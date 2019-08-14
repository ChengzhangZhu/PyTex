# PyTex Package

The *PyTex* package provides a serial of tools for latex processing.
It aims to help academic fellows to improve manuscript writing efficiency.

# Available Tools
+ `table2csv(file_path, end_pattern=None, head=False, save_name='latex_table')`
    + `file_path`: str, the latex table path
    + `end_pattern`: str, the pattern at the end of each line
    + `head`: bool, whether the head line involved in the table
    + `save_name`: str, save name of the csv file; the default is 'latex_table'
    + `output`: None, generate a csv file as the save name 