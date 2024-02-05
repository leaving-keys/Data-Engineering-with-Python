"""
Reading a *.json file using pandas.
"""
import pandas
import os

with open(os.path.join("json_files", "data.json")) as file:
    json_string = file.read()
    json_data = pandas.io.json.loads(json_string)
    df = pandas.json_normalize(json_data, record_path="records")
    
    print(df.head(2).to_json(orient="columns"))
    print()
    print(df.head(2).to_json(orient="records"))
