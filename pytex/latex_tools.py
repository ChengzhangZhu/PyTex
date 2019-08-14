import pandas as pd
import numpy as np

__all__ = ['table2csv']


def table2csv(file_path, end_pattern=None, head=False, save_name='latex_table'):
    """
    Transform latex table to Excel editable csv file
    :param file_path: str, the latex table path
    :param end_pattern: str, the pattern at the end of each line
    :param head: bool, whether the head line involved in the table
    :param save_name: str, save name of the csv file; the default is 'latex_table'
    :return: generate a csv file as the save name
    """
    if end_pattern is None:
        end_pattern = '\\\\'

    with open(file_path, 'r') as f:
        content = f.readlines()
    head_log = False
    content_lines = list()
    for line in content:
        if end_pattern in line:
            if head and not head_log:  # read head line
                head_list = _read_line_content(line.strip()[:-len(end_pattern)])
                head_log = True
            else:
                content_line = _read_line_content(line.strip()[:-len(end_pattern)])
                content_lines.append(content_line)
    assert len(content_lines) > 0, 'No data has been loaded!'
    dim = len(content_lines[0])
    content_list = []
    for i in range(dim):
        content_list.append([content[i] for content in content_lines])
    if not head:
        head_list = np.r_[0:dim]
    content_dict = dict()
    for index, head_content in enumerate(head_list):
        content_dict[head_content] = content_list[index]
    data_frame = pd.DataFrame(content_dict, columns=head_list)
    data_frame.to_csv(save_name+'.csv', header=head, index=False)


def _read_line_content(line):
    content = line.split('&')
    content = [_clean_content(i) for i in content]
    return content


def _clean_content(content):
    content = content.strip(' ')
    content = content.strip()
    # clean math environment
    content = content.strip('$')
    # clean highlight
    clean_flag = True
    while clean_flag:
        content, clean_flag = _remove_latex_commend(content, ['\\textbf{}', '\\mathbf{}',
                                                              '\\bm{}', '\\textit{}'])
    return content


def _remove_latex_commend(content, commend_list):
    removed_flag = False
    for commend in commend_list:
        commend = commend[:-1]
        if content[0:len(commend)] == commend:
            content = content[len(commend):-1]
            removed_flag = True
    return content, removed_flag
