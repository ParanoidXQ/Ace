import pandas as pd
import numpy as np


def num2vec(df1):
    print("Num2vec is initiating.")
    df2 = pd.DataFrame(
        columns=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', 'Flag'])
    lh = df1.shape[0]
    ary1 = np.zeros((lh * 21, 21))
    df3 = df2.append(pd.DataFrame(ary1,
                                  columns=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                                           '15', '16', '17', '18', '19', '20', 'Flag']), ignore_index=True)
    k = 1
    for i in range(0, lh):
        df3.loc[21 * i, 'Flag'] = df1.loc[i, 'Flag']
        for j in range(0, 21):
            df3.iloc[21 * i + j, int(df1.loc[i, str(j + 1)]) - 1] = 1
        if i + 1 == round(k * lh / 10):
            print("{}% has been processed.".format(k * 10))
            k += 1
    print('\n')
    return df3
