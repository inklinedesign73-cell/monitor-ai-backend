import requests
from bs4 import BeautifulSoup

BASE_URL = "https://monitoruloficial.ro"

def fetch_documents():
    url = f"{BASE_URL}/ro/free-monitor"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    documents = []

    # căutăm orice text relevant (nu doar PDF)
    for item in soup.find_all("a"):
        text = item.get_text(strip=True)
        href = item.get("href")

        if text and len(text) > 10:
            documents.append({
                "title": text,
                "link": href if href else ""
            })

    return documents[:10]
