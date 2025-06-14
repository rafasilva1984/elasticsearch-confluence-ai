import json, os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()
es = Elasticsearch(
    hosts=[os.getenv("ELASTIC_URL")],
    basic_auth=(os.getenv("ELASTIC_USER"), os.getenv("ELASTIC_PASSWORD")),
    verify_certs=False
)

with open("data_cleaned.json") as f:
    docs = json.load(f)

for doc in docs:
    es.index(index="confluence_docs", document=doc)
