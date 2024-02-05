from elasticsearch import Elasticsearch
from elasticsearch import helpers
from faker import Faker
from dotenv import find_dotenv, dotenv_values


env_vars = dotenv_values(find_dotenv())
es = Elasticsearch(env_vars["ELASTICSEARCH_URL"])
fake = Faker()
actions = [{
    "_index": "users",
    "_source": {
        "name": fake.name(),
        "street": fake.street_address(),
        "city": fake.city(),
        "zip": fake.zipcode(),
    }
} for i in range(1000)]
res = helpers.bulk(es, actions)
print(res)
