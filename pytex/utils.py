import numpy as np
import pandas as pd


def table2rank(table, transpose=False, is_large_value_high_performance=True, add_averaged_rank=False):
    """
    transform a performance value table to a rank table
    :param table: pandas DataFrame or numpy array, the table with performance values
    :param transpose: bool, whether to transpose table (default: False; the method is column and data set is row)
    :param is_large_value_high_performance: bool, whether a larger value has higher performance
    :param add_averaged_rank: bool, whether add averaged ranks after the last row/column
    :return: a rank table (numpy.array or pd.DataFrame)
    """
    table = table.copy()
    if isinstance(table, pd.DataFrame):
        column_name = table.columns.values
        if table.iloc[:, 0].dtype == 'object':
            index_name = table.iloc[:, 0].values
            table = table.iloc[:, 1:]
        else:
            index_name = None
        data = table.values
    else:
        data = table
    if transpose:
        data = data.transpose()
    # rank each row
    rank_table = list()
    for row in data:
        if is_large_value_high_performance:
            index = np.argsort(-row)
        else:
            index = np.argsort(row)
        rank = np.zeros(len(index))
        for i, value in enumerate(index):
            if i > 0:
                if row[value] == row[index[i - 1]]:
                    rank[value] = i - 1
                    continue
            rank[value] = i
        rank += 1
        rank_table.append(rank)
    rank_table = np.asarray(rank_table)
    if add_averaged_rank:
        averaged_rank = [np.mean(rank_table[:, i]) for i in range(rank_table.shape[1])]
        rank_table = np.concatenate([rank_table, np.asarray([averaged_rank])])
    if transpose:
        rank_table = rank_table.transpose()
    if isinstance(table, pd.DataFrame):  # reconstruct the pandas table
        if index_name is not None:
            if add_averaged_rank:
                if not transpose:
                    index_name = np.concatenate([index_name, np.array(['AR'])])
                else:
                    column_name = np.concatenate([column_name, np.asarray(['AR'])])
            rank_table = np.concatenate([index_name[:, np.newaxis], rank_table], axis=1)
        rank_table = pd.DataFrame(data=rank_table, columns=column_name)
    return rank_table
