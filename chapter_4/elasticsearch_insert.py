from elasticsearch import Elasticsearch
from faker import Faker
from dotenv import find_dotenv, dotenv_values


env_vars = dotenv_values(find_dotenv())
fake = Faker()
es = Elasticsearch(env_vars["ELASTICSEARCH_URL"])
doc = {
    "name": fake.name(),
    "street": fake.street_address(),
    "city": fake.city(),
    "zip": fake.zipcode(),
}
res = es.index(index="users", document=doc)
print(res['result'])
