"""
Writing a *.csv file using the csv library.
"""
import csv

with open("csv_files/my_csv.csv", mode="w") as output:
    csv_writer = csv.writer(output)

    header = ["name", "age"]
    csv_writer.writerow(header)

    data = ["Bob Smith", 40]
    csv_writer.writerow(data)
