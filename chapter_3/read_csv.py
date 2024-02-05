"""
Print some information from a *.csv file using the csv library.
"""
import csv
import os

with open(os.path.join("csv_files", "data.csv")) as file:
    csv_reader = csv.DictReader(file)

    print(csv_reader.fieldnames)
    for row in csv_reader:
        print(row["name"])
