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

        # 🔴 păstrăm DOAR linkuri interne relevante
        if not link.startswith("/"):
            continue

        # 🔴 filtrăm doar secțiuni utile
        allowed = [
            "pierderi",
            "concursuri",
            "anunturi",
            "acte",
            "persoane"
        ]

        if not any(word in link.lower() for word in allowed):
            continue

        if len(title) < 5:
            continue

        full_link = BASE_URL + link

        documents.append({
            "title": title,
            "url": full_link
        })

    return documents[:20]