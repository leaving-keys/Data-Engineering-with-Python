from elasticsearch import Elasticsearch
import pandas
from dotenv import find_dotenv, dotenv_values


env_vars = dotenv_values(find_dotenv())
es = Elasticsearch(env_vars["ELASTICSEARCH_URL"])
query = {
    "match_all": {}
}
res = es.search(index="users", query=query, size=10)
df = pandas.json_normalize(res['hits']['hits'])
print(df.head())
