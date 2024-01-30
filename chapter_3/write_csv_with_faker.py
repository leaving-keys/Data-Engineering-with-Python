"""
Writing a *.csv file using the faker library to generate some user data.
"""
import csv

from faker import Faker

with open("csv_files/data.csv", "w") as output:
    fake = Faker()
    csv_writer = csv.writer(output)

    header = ["name", "age", "street", "city", "state", "zip", "lng", "lat"]
    csv_writer.writerow(header)

    for r in range(1000):
        data = [
            fake.name(),
            fake.random_int(min=18, max=80, step=1),
            fake.street_address(),
            fake.city(),
            fake.state(),
            fake.zipcode(),
            fake.longitude(),
            fake.latitude(),
        ]
        csv_writer.writerow(data)
