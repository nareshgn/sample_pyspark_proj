import pandas as pd
import pyarrow.parquet as pq


def convert_xlsx_to_csv():
    data = pd.read_excel("data/sample_data.xlsx", index_col=False)
    df = pd.DataFrame(data=data)
    # df['id'] = df['id'].astype(pd.Int32Dtype())
    # remove all Null values and replace with
    df = df.replace(['NULL'], '')
    print(df)

    df.to_csv('data/csvfile.csv', encoding='utf-8', index=False, header=True)

    file_in = open("data/csvfile.csv", "rt")
    # output file to write the result to
    file_out = open("data/formatted_csvfile.csv", "wt")
    for line in file_in:
        # read replace the string and write to output file
        file_out.write(line.replace(',', '||'))
    # close input and output files
    file_in.close()
    file_out.close()

    print('------This is formatted CSV data-----')
    data = pd.read_csv("data/formatted_csvfile.csv", index_col=False, header=0)
    print(data)


def convert_csv_to_parquet():
    data = pd.read_csv("data/csvfile.csv", index_col=False)
    df = pd.DataFrame(data=data)
    df.to_parquet('data/sample_data-original.parquet')

    df_parquet = pq.read_table(source='data/sample_data-original.parquet').to_pandas()
    print(df_parquet)


def compare_data():
    data = pd.read_csv("data/csvfile.csv", index_col=False)
    df = pd.DataFrame(data=data)
    print("\nThe number of row count in original file:", len(df))
    print("The number of column count in original file:", len(df.columns))

    data = pd.read_csv("data/datasource_csvfile.csv", index_col=False)
    df_db = pd.DataFrame(data=data)
    print("\nThe number of row count from database:", len(df_db))
    print("The number of column count from database:", len(df_db.columns))

    assert len(df) == len(df_db), 'Num of rows does not match with original data'
    assert len(df.columns) == len(df_db.columns), 'Num of columns does not match with original data'


