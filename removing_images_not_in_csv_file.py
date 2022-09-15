import os
import pandas as pd

path = "cicekci-bpr"
#pd.read_csv('C:/Users/hakan/OneDrive/Masaüstü/silinecek/urunler2.csv', encoding = 'ISO-8859-1', on_bad_lines='skip')
flist = pd.read_csv('urunler2.csv', encoding = 'ISO-8859-1', on_bad_lines='skip')

file_name = flist['buyukresim'].tolist()

for buyukresim in os.listdir(path):
    if buyukresim not in file_name:
        print(buyukresim)
        full_file_path = os.path.join(path, buyukresim)
        os.remove(full_file_path)
        #if buyukresim not in file_name:
            #os.remove(buyukresim)
