import json
from bs4 import BeautifulSoup

with open("data_raw.json") as f:
    data = json.load(f)

docs = []
for result in data.get("results", []):
    content = BeautifulSoup(result["body"]["storage"]["value"], "html.parser").get_text()
    docs.append({
        "id": result["id"],
        "title": result["title"],
        "space": result["space"]["key"],
        "url": f'{result["_links"]["base"]}{result["_links"]["webui"]}',
        "content": content
    })

with open("data_cleaned.json", "w") as f:
    json.dump(docs, f)
