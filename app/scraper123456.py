import requests
from bs4 import BeautifulSoup

BASE_URL = "https://monitoruloficial.ro"


def fetch_documents():
    url = BASE_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    documents = []

    # 🔍 extragem toate link-urile
    for a in soup.find_all("a"):
        title = a.get_text(strip=True)
        link = a.get("href")

        # 🔴 filtrare
        if not title or not link:
            continue

        if len(title) < 15:
            continue

        if link == "#":
            continue

        # 🔗 transformăm în link complet
        if not link.startswith("http"):
            link = BASE_URL + link

        documents.append({
            "title": title,
            "url": link
        })

    # limităm pentru stabilitate
    return documents[:20]