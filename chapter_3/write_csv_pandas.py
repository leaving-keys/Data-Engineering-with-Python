"""
Writing a *.csv file using pandas.
"""
import pandas

data = {
    "Name": ["Paul", "Bob", "Susan", "Yolanda"],
    "Age": [23, 45, 18, 21],
}
df = pandas.DataFrame(data)
df.to_csv("csv_files/from_df.csv", index=False)
