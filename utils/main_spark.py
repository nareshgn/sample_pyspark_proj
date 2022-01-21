from datetime import datetime

import pyspark as s
from pyspark import *
import pandas as pd

# sc = SparkContext()
# sql = SQLContext(sc)
from pyspark.sql import SparkSession


def read_files():
    spark = SparkSession.builder.appName('PySpark Demo').getOrCreate()
    # df_excel = spark.read.format("com.crealytics.spark.excel") \
    #     .option("header", "true") \
    #     .option("inferSchema", "true") \
    #     .load('sample_data.xlsx')

    pd_df = pd.read_excel('data/sample_data.xlsx')
    df_excel = spark.createDataFrame(pd_df.astype(str))

    print('------This is Excel data-----')
    print(df_excel.show())

    df_csv = spark.read.csv("data/csvfile.csv", header=True)
    print('------This is CSV data-----')
    print(df_csv.show())

    parquet_filename = "data/sample_data_" + str(datetime.now()) + ".parquet"
    df_csv.write.parquet(parquet_filename)
    df_parquet = spark.read.parquet(parquet_filename)
    print('------This is parquet data-----')
    print(df_parquet.show())


def compare_data():
    spark = SparkSession.builder.appName('PySpark Demo').getOrCreate()
    # df_excel = spark.read.format("com.crealytics.spark.excel") \
    #     .option("header", "true") \
    #     .option("inferSchema", "true") \
    #     .load('sample_data.xlsx')

    df_csv = spark.read.csv("data/csvfile.csv", header=True)
    print("The number of row count in original file:", df_csv.count())
    print("The number of column count in original file:", len(df_csv.columns))

    df_db = spark.read.csv("data/csvfile.csv", header=True)
    print("The number of row count from database:", df_db.count())
    print("The number of column count from database:", len(df_db.columns))

    assert df_csv.count() == df_db.count(), 'Num of rows does not match with original data'
