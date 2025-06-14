import os, requests, json
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()
BASE_URL = os.getenv("CONFLUENCE_BASE_URL")
USER = os.getenv("CONFLUENCE_USER")
TOKEN = os.getenv("CONFLUENCE_API_TOKEN")

def get_pages(space_key="DOC"):
    url = f"{BASE_URL}/rest/api/content"
    params = {"spaceKey": space_key, "expand": "body.storage", "limit": 100}
    auth = HTTPBasicAuth(USER, TOKEN)
    r = requests.get(url, params=params, auth=auth, verify=False)
    return r.json()

with open("data_raw.json", "w") as f:
    json.dump(get_pages(), f)
