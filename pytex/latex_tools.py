import pandas as pd
import numpy as np

__all__ = ['table2csv', 'csv2latex']


def table2csv(file_path, end_pattern=None, head=False, save_name='latex_table', clean_pattern=None):
    """
    Transform latex table to Excel editable csv file
    :param file_path: str, the latex table path
    :param end_pattern: str, the pattern at the end of each line
    :param head: bool, whether the head line involved in the table
    :param save_name: str, save name of the csv file; the default is 'latex_table'
    :param clean_pattern: list, specific the clean patterns;
                          the default is ['\\textbf{}', '\\mathbf{}', '\\bm{}', '\\textit{}']
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
                head_list = _read_line_content(line.strip()[:-len(end_pattern)], clean_pattern=clean_pattern)
                head_log = True
            else:
                content_line = _read_line_content(line.strip()[:-len(end_pattern)], clean_pattern=clean_pattern)
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


def csv2latex(file_path, head=True, save_name='csv_latex', replace=None):
    """
    Transform a table with csv file to latex code
    :param file_path: str, the csv file path
    :param head: bool, whether the table contains a header; default is True
    :param save_name: str, the generated latex code name
    :param replace: dict, a replace dict; if given, the key in the table will be replaced by the value; default is None
    :return: generate a file of latex code
    """
    if head:
        data = pd.read_csv(file_path)
    else:
        data = pd.read_csv(file_path, header=None)
    if replace is None:
        replace = dict()
    head_list = data.columns.to_list()
    content = data.values
    write_content = []
    with open(save_name, 'w') as f:
        if head:
            write_content.append('\\toprule')
            # construct header
            header_content = ''
            for index, item in enumerate(head_list):
                header_content += str(replace[item] if item in replace else item)
                if index != len(head_list) - 1:
                    header_content += '  &  '
                else:
                    header_content += '  \\\\'
            write_content.append(header_content)
            write_content.append('\\midrule')
        # construct content
        for line_index, line in enumerate(content):
            line_content = ''
            for index, item in enumerate(line):
                line_content += str(replace[item] if item in replace else item)
                if index != len(line) - 1:
                    line_content += '  &  '
                else:
                    line_content += '  \\\\'
                    write_content.append(line_content)
            if line_index == len(content) - 1:
                write_content.append('\\bottomrule')
        f.writelines("%s\n" % l for l in write_content)


def _read_line_content(line, clean_pattern=None):
    content = line.split('&')
    content = [_clean_content(i, clean_pattern=clean_pattern) for i in content]
    return content


def _clean_content(content, clean_pattern=None):
    if clean_pattern is None:
        clean_pattern = ['\\textbf{}', '\\mathbf{}', '\\bm{}', '\\textit{}']
    assert isinstance(clean_pattern, list), 'Clean pattern should be given by list.'
    content = content.strip(' ')
    content = content.strip()
    # clean math environment
    content = content.strip('$')
    # clean highlight
    clean_flag = True
    while clean_flag:
        content, clean_flag = _remove_latex_commend(content, clean_pattern)
    return content


def _remove_latex_commend(content, commend_list):
    removed_flag = False
    for commend in commend_list:
        commend = commend[:-1]
        if content[0:len(commend)] == commend:
            content = content[len(commend):-1]
            removed_flag = True
    return content, removed_flag
