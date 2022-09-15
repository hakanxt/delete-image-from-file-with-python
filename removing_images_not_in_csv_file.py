import os
import pandas as pd

path = "images"
flist = pd.read_csv('my_sql_table.csv', encoding = 'ISO-8859-1', on_bad_lines='skip')

file_name = flist['column_name'].tolist()

for column_name in os.listdir(path):
    if column_name not in file_name:
        print(column_name)
        full_file_path = os.path.join(path, column_name)
        os.remove(full_file_path)

