import os
import sys
from pathlib import Path

import pandas as pd
import glob

file_location = os.path.join('data/', 'second_table.xlsx')
filenames = glob.glob(file_location)

for file in filenames:
    df = pd.read_excel(file)
    df = df.replace(['NULL'], '')

    file_name = Path(file).stem
    df.to_csv('data/' + file_name + '.csv', encoding='utf-8', index=False, header=True)
    df.to_parquet('data/expected_data/' + file_name + '.parquet')

    # file_in = open('data/'+file_name+'.csv', 'rt')
    # # output file to write the result to
    # file_out = open('data/'+file_name+'_formatted.csv', "wt")
    # for line in file_in:
    #     # read replace the string and write to output file
    #     file_out.write(line.replace(',', '||'))
    # # close input and output files
    # file_in.close()
    # file_out.close()