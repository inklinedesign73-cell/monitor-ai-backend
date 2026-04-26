import requests
from bs4 import BeautifulSoup

BASE_URL = "https://monitoruloficial.ro"


def fetch_documents():
    print("SCRAPER VERSION 2 LOADED")  # 🔥 debug - verificăm deploy

    try:
        response = requests.get(BASE_URL, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        documents = []

        # 🔍 extragem toate link-urile din pagină
        for a in soup.find_all("a"):
            title = a.get_text(strip=True)
            link = a.get("href")

            # 🔴 filtrări esențiale
            if not title or not link:
                continue

            if len(title) < 15:
                continue

            if link == "#" or link.startswith("javascript"):
                continue

            # 🔗 transformăm link relativ în absolut
            if not link.startswith("http"):
                link = BASE_URL + link

            documents.append({
                "title": title,
                "url": link
            })

        # 🔒 limităm pentru stabilitate
        return documents[:20]

    except Exception as e:
        print("SCRAPER ERROR:", e)
        return []