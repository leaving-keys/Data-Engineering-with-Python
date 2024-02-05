"""
Reading a *.json file using the json library.
"""
import json
import os

with open(os.path.join("json_files", "data.json"), "r") as file:
    data = json.load(file)
    print(data["records"][0])
    print(data["records"][0]["name"])
