import numpy as np


def build_dataset(series, seq_length):
    data_x = []
    data_y = []
    for i in range(0, len(series) // seq_length):
        _x = series[i * seq_length: i * seq_length + seq_length, : -1]
        _y = series[i * seq_length, [-1]]
        #         print(_x, "->", _y)
        data_x.append(_x)
        data_y.append(_y)
    return np.array(data_x), np.array(data_y)
