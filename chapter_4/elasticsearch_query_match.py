from elasticsearch import Elasticsearch
from dotenv import find_dotenv, dotenv_values


env_vars = dotenv_values(find_dotenv())
es = Elasticsearch(env_vars["ELASTICSEARCH_URL"])
query = {
    "bool": {
        "should": [{
            "term": { "name": "murphy" }
        }
        , {
            "term": { "name": "earl" }
        }]
    }
}
res = es.search(index="users", query=query, size=10)
for row in res['hits']['hits']:
    print(row['_source'])
