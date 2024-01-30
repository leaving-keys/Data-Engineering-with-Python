"""
Using pandas to read a *.csv file.
"""
import pandas

df = pandas.read_csv("csv_files/data.csv")
print(df.head(10))
