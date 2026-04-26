import requests
from bs4 import BeautifulSoup

BASE_URL = "https://monitoruloficial.ro"


def fetch_documents():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    documents = []

    for a in soup.find_all("a"):
        title = a.get_text(strip=True)
        link = a.get("href")

        if not title or not link:
            continue

        # 🔴 ignorăm link-uri externe
        if link.startswith("http") and "monitoruloficial.ro" not in link:
            continue

        # 🔴 ignorăm junk
        if len(title) < 10:
            continue

        if link == "#" or link.startswith("javascript"):
            continue

        # 🔗 transformăm în link complet
        if not link.startswith("http"):
            link = BASE_URL + link

        documents.append({
            "title": title,
            "url": link
        })

    return documents[:20]