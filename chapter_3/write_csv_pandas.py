"""
Writing a *.csv file using pandas.
"""
import pandas
import os

data = {
    "Name": ["Paul", "Bob", "Susan", "Yolanda"],
    "Age": [23, 45, 18, 21],
}
df = pandas.DataFrame(data)
df.to_csv(os.path.join("csv_files", "from_df.csv"), index=False)
