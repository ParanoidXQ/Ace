import pandas as pd


def char2num(df1, f):
    print("Char2num is initiating.")
    df2 = df1.loc[df1.Len == 21].reset_index(drop=True)
    df3 = pd.DataFrame(
        columns=['Entry', 'Position', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                 '16', '17', '18', '19', '20', '21', 'Flag'])
    df3.loc[:, 'Entry'] = df2.loc[:, 'Entry']
    df3.loc[:, 'Position'] = df2.loc[:, 'Position']
    df3.loc[:, 'Flag'] = f
    lh = df2.shape[0]
    k = 1
    for i in range(0, lh):
        for j in range(0, 21):
            if ord(df2.loc[i, 'Sequence'][j]) == 65:
                df3.iloc[i, j + 2] = 1
            elif 66 < ord(df2.loc[i, 'Sequence'][j]) < 74:
                df3.iloc[i, j + 2] = ord(df2.loc[i, 'Sequence'][j]) - 65
            elif 74 < ord(df2.loc[i, 'Sequence'][j]) < 79:
                df3.iloc[i, j + 2] = ord(df2.loc[i, 'Sequence'][j]) - 66
            elif 79 < ord(df2.loc[i, 'Sequence'][j]) < 85:
                df3.iloc[i, j + 2] = ord(df2.loc[i, 'Sequence'][j]) - 67
            elif 85 < ord(df2.loc[i, 'Sequence'][j]) < 88:
                df3.iloc[i, j + 2] = ord(df2.loc[i, 'Sequence'][j]) - 68
            elif ord(df2.loc[i, 'Sequence'][j]) == 89:
                df3.iloc[i, j + 2] = 20
            else:
                print('Wrong input in row {} column {}.'.format(i, j))
        if i + 1 == round(k * lh / 10):
            print("{}% has been processed.".format(k * 10))
            k += 1
    print('\n')
    return df3
