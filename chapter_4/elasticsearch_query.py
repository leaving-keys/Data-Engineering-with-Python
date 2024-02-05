from elasticsearch import Elasticsearch
from dotenv import find_dotenv, dotenv_values


env_vars = dotenv_values(find_dotenv())
es = Elasticsearch(env_vars["ELASTICSEARCH_URL"])
query = {
    "match_all": {}
}
res = es.search(index="users", query=query, size=5)
print(res['hits']['hits'])
for doc in res['hits']['hits']:
    print(doc['_source'])
