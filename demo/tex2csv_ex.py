from pytex.latex_tools import table2csv, csv2latex

table2csv('latex_table', head=True, save_name='latex_csv')
table2csv('latex_table', head=True, save_name='chapter_6_results', clean_pattern=[])
csv2latex('latex_csv.csv', head=True, save_name='latex_code')