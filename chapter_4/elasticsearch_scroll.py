from elasticsearch import Elasticsearch
from dotenv import find_dotenv, dotenv_values


env_vars = dotenv_values(find_dotenv())
es = Elasticsearch(env_vars["ELASTICSEARCH_URL"])
query = {
    "match_all": {}
}
res = es.search(
    index="users",
    scroll="20m",
    size=100,
    query=query,
)
scroll_id = res["_scroll_id"]
size = res["hits"]["total"]["value"]
with open("output.txt", "w") as output:
    while (size > 0):
        for doc in res["hits"]["hits"]:
            print(doc["_source"])
        res = es.scroll(scroll_id=scroll_id, scroll="20m")
        scroll_id = res["_scroll_id"]
        size = len(res["hits"]["hits"])
