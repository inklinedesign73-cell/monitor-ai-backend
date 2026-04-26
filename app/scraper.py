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

        # 🔴 ignorăm link-uri inutile
        if link == "#" or link.startswith("javascript"):
            continue

        # 🔴 ignorăm texte scurte
        if len(title) < 10:
            continue

        # 🔴 filtrăm doar cuvinte relevante
        keywords = [
            "pierderi",
            "persoane",
            "anunțuri",
            "acte",
            "concurs",
            "posturi"
        ]

        if not any(word in title.lower() for word in keywords):
            continue

        # 🔗 link complet
        if not link.startswith("http"):
            link = BASE_URL + link

        documents.append({
            "title": title,
            "url": link
        })

    return documents[:20]