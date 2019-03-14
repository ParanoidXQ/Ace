import tensorflow as tf
from char_ext import *
from char2num import *
from num2vec import *
from rand_sort import *
from build_dataset import *

Ace_df1 = pd.read_excel('Ace.xlsx')
Un_df1 = pd.read_excel('UnAce.xlsx')
Un_df2 = char_ext(Un_df1)
Ace_df2 = char2num(Ace_df1, 1)
Un_df3 = char2num(Un_df2, 0)
Ace_df3 = num2vec(rand_sort(Un_df3, Ace_df2))
# Ace_df3.to_csv('Exp.csv')
xy = Ace_df3.values
seq_length = 21
data_dim = 20
hidden_dim = 100
output_dim = 1
learning_rate = 0.01
iterations = 500
train_size = int((len(xy) / seq_length) * 0.7) * seq_length
train_set = xy[0:train_size]
test_set = xy[train_size:]
trainX, trainY = build_dataset(train_set, seq_length)
testX, testY = build_dataset(test_set, seq_length)
X = tf.placeholder(tf.float32, [None, seq_length, data_dim])
Y = tf.placeholder(tf.float32, [None, 1])
cell = tf.nn.rnn_cell.LSTMCell(
    num_units=hidden_dim, state_is_tuple=True, activation=tf.tanh)
outputs, _states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)
Y_pred = tf.layers.dense(outputs[:, -1], output_dim, activation=tf.sigmoid)
# cost/loss
loss = -tf.reduce_mean(
    Y * tf.log(tf.clip_by_value(Y_pred, 1e-10, 1.0)) + (1 - Y) * tf.log(tf.clip_by_value(1 - Y_pred, 1e-10, 1.0)))
# optimizer
optimizer = tf.train.AdamOptimizer(learning_rate)
train = optimizer.minimize(loss)

correct_prediction = tf.equal((Y_pred > 0.5), trainY)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

    # Training step
    for i in range(iterations):
        _, step_loss = sess.run([train, loss], feed_dict={
            X: trainX, Y: trainY})
        accuracy_ = sess.run(accuracy, {X: trainX, Y: trainY})
        print("[step: {}] loss: {} accuracy: {}".format(i, step_loss, accuracy_))

    yy = sess.run(Y_pred, feed_dict={X: testX})
    test_accuracy = sess.run(tf.reduce_mean(tf.cast(tf.equal((yy > 0.5), testY), 'float')))
    print("[test accuracy: {}".format(test_accuracy))

    ch1 = 'A'
    while ch1 != 'Z':
        ch1 = input('请输入要检测的序列（输入Z结束）：')
        if len(ch1) != 21:
            print("End.")
            break
        df_x = pd.DataFrame(columns=['Entry', 'Position', 'Sequence', 'Len'])
        df_x = df_x.append(pd.DataFrame([['Test1', '11', ch1, 21]], columns=['Entry', 'Position', 'Sequence', 'Len']),
                           ignore_index=True)
        ary_x = num2vec(char2num(df_x, 1)).values
        ary_x1 = ary_x[:, :-1].reshape(1, 21, 20)
        y_x = sess.run(Y_pred, feed_dict={X: ary_x1})
        if 0.5 < y_x[0][0] <= 1:
            print('y = {}，此处为乙酰化位点'.format(y_x[0][0]))
        elif 0 <= y_x[0][0] <= 0.5:
            print('y = {}，此处为非乙酰化位点'.format(y_x[0][0]))
        else:
            print('Error')
            break
