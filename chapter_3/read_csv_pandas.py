"""
Using pandas to read a *.csv file.
"""
import pandas
import os

df = pandas.read_csv(os.path.join("csv_files","data.csv"))
print(df.head(10))
