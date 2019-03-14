import pandas as pd


def char_ext(df1):
    print("Char extracting is initiating.")
    df2 = pd.DataFrame(columns=['Entry', 'Position', 'Sequence', 'Len'])
    lg = df1.shape[0]
    k = 1
    for i in range(0, lg):
        for j in range(0, df1.loc[i, 'Length']):
            if df1.Sequence[i][j] == 'K':
                if 9 < j < df1.loc[i, 'Length'] - 10:
                    df2 = df2.append(
                        pd.DataFrame([[df1.loc[i, 'Entry'], j + 1, df1.loc[i, 'Sequence'][j - 10:j + 11], 21]],
                                     columns=['Entry', 'Position', 'Sequence', 'Len']), ignore_index=True)
                elif j < 10 and j < df1.loc[i, 'Length'] - 10:
                    df2 = df2.append(
                        pd.DataFrame([[df1.loc[i, 'Entry'], j + 1, df1.loc[i, 'Sequence'][:j + 11], j + 11]],
                                     columns=['Entry', 'Position', 'Sequence', 'Len']), ignore_index=True)
                elif 9 < j and df1.loc[i, 'Length'] - 11 < j:
                    df2 = df2.append(
                        pd.DataFrame([[df1.loc[i, 'Entry'], j + 1, df1.loc[i, 'Sequence'][j - 10:],
                                       df1.loc[i, 'Length'] - j + 10]],
                                     columns=['Entry', 'Position', 'Sequence', 'Len']), ignore_index=True)
                else:
                    df2 = df2.append(
                        pd.DataFrame([[df1.loc[i, 'Entry'], j + 1, df1.loc[i, 'Sequence'], df1.loc[i, 'Length']]],
                                     columns=['Entry', 'Position', 'Sequence', 'Len']), ignore_index=True)
        if i + 1 == round(k * lg / 10):
            print("{}% has been processed.".format(k * 10))
            k += 1
    print('\n')
    return df2
