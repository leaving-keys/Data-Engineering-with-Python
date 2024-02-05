"""
Print some information from a *.csv file using the csv library.
"""
import csv

with open("csv_files/data.csv") as file:
    csv_reader = csv.DictReader(file)

    print(csv_reader.fieldnames)
    for row in csv_reader:
        print(row["name"])
