# import pyspark as s
# from pyspark import *
import pandas as pd

# from pyspark.sql import SparkSession

# spark = SparkSession.builder.appName('PySpark Demo').getOrCreate()
pd_df = pd.read_excel('data/sample_data.xlsx')
# spark_df = spark.createDataFrame(pd_df.astype(str))
# spark_df.coalesce(1).write.mode('overwrite').csv("data/", header=True, encoding='utf-8')

pd_df.to_csv('data/csvfile.csv', encoding='utf-8', index=False, header=True)

file_in = open("data/csvfile.csv", "rt")
# output file to write the result to
file_out = open("data/formatted_csvfile.csv", "wt")
for line in file_in:
    # read replace the string and write to output file
    file_out.write(line.replace(',', '||'))
# close input and output files
file_in.close()
file_out.close()