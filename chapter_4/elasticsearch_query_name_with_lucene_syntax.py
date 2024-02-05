from elasticsearch import Elasticsearch
from dotenv import find_dotenv, dotenv_values


env_vars = dotenv_values(find_dotenv())
es = Elasticsearch(env_vars["ELASTICSEARCH_URL"])
res = es.search(index="users", q="name:Kevin Davis", size=10)
for row in res["hits"]["hits"]:
    print(row["_source"])
