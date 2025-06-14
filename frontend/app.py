from flask import Flask, request, render_template
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

es_url = os.getenv("ELASTIC_URL")
es_user = os.getenv("ELASTIC_USER")
es_pass = os.getenv("ELASTIC_PASSWORD")

if not es_url:
    raise ValueError("Variável ELASTIC_URL não definida no .env")

es = Elasticsearch(
    hosts=[es_url],
    basic_auth=(es_user, es_pass),
    verify_certs=False
)

model = SentenceTransformer(r"C:\Users\rafael.silva\paraphrase-MiniLM-L6-v2")

@app.route("/", methods=["GET", "POST"])
def search():
    results = []
    if request.method == "POST":
        query = request.form["query"]
        vector = model.encode(query).tolist()
        body = {
            "size": 5,
            "knn": {
                "field": "vector",
                "k": 5,
                "num_candidates": 100,
                "query_vector": vector
            }
        }
        res = es.search(index="confluence_docs", body=body)
        results = res["hits"]["hits"]
    return render_template("search.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
