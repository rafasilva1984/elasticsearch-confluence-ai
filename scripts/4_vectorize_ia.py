import json, os
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()
es = Elasticsearch(
    hosts=[os.getenv("ELASTIC_URL")],
    basic_auth=(os.getenv("ELASTIC_USER"), os.getenv("ELASTIC_PASSWORD")),
    verify_certs=False
)
model = SentenceTransformer(r"C:\Users\rafael.silva\paraphrase-MiniLM-L6-v2")

with open("data_cleaned.json") as f:
    docs = json.load(f)

for doc in docs:
    vector = model.encode(doc["content"]).tolist()
    es.update(index="confluence_docs", id=doc["id"], body={"doc": {"vector": vector}})
