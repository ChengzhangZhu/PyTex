from pytex.latex_tools import table2csv, csv2latex

table2csv('latex_table', head=True, save_name='latex_csv')
csv2latex('latex_csv.csv', head=True, save_name='latex_code')