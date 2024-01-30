"""
Writing a *.json file using Faker to create randomly generated user data.
"""
import json

with open("json_files/data.json", "w") as output:
    fake = Faker()
    all_data = {}
    all_data["records"] = []

    for x in range(1_000):
        data = {
            "name": fake.name(),
            "age": fake.random_int(min=18, max=80, step=1),
            "street": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "zip": fake.zipcode(),
            "lng": float(fake.longitude()),
            "lat": float(fake.latitude()),
        }
        all_data["records"].append(data)
    json.dump(all_data, output)