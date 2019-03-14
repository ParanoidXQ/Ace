import pandas as pd


def rand_sort(df1, df2):
    df3 = pd.concat([df1, df2], ignore_index=True)
    df4 = df3.sample(frac=1).reset_index(drop=True)
    return df4
