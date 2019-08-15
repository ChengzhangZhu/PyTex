# PyTex Package

The *PyTex* package provides a serial of tools for latex processing.
It aims to help academic fellows to improve manuscript writing efficiency.

# Install
Go into *dist* folder and execute:
`python -m pip install pytex-0.0.5-py3-none-any.whl`

# How to use
See demos in *demo* folder.

# Available Tools
+ `table2csv(file_path, end_pattern=None, head=False, save_name='latex_table', clean_pattern=None)`
    Transform latex table to Excel editable csv file
    + `file_path`: str, the latex table path
    + `end_pattern`: str, the pattern at the end of each line
    + `head`: bool, whether the head line involved in the table
    + `save_name`: str, save name of the csv file; the default is 'latex_table'
    + `clean_pattern`: list, specific the clean patterns; 
                       the default is ['\\textbf{}', '\\mathbf{}', '\\bm{}', '\\textit{}']
    + `output`: None, generate a csv file as the save name 

+ `csv2latex(file_path, head=True, save_name='csv_latex')`
    Transform a table with csv file to latex code
    + `file_path`: str, the csv file path
    + `head`: bool, whether the table contains a header; default is True
    + `save_name`: str, the generated latex code name
    + `output`: None, generate a file of latex code