from elasticsearch import Elasticsearch
from dotenv import find_dotenv, dotenv_values


env_vars = dotenv_values(find_dotenv())
es = Elasticsearch(env_vars["ELASTICSEARCH_URL"])
print(es.info())
