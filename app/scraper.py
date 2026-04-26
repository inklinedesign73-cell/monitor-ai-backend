import requests
from bs4 import BeautifulSoup

URLS = [
    "https://monitoruloficial.ro/pierderi-persoane-fizice/",
    "https://monitoruloficial.ro/pierderi-persoane-juridice/",
    "https://monitoruloficial.ro/concursuri-posturi-publice/",
    "https://monitoruloficial.ro/anunturi-profesionisti/",
    "https://monitoruloficial.ro/publicare-acte-normative/"
]


def fetch_documents():
    documents = []

    for url in URLS:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            # 🔥 luam titlul paginii ca document
            title = soup.title.string.strip() if soup.title else url

            documents.append({
                "title": title,
                "url": url
            })

        except Exception as e:
            print("ERROR:", e)

    return documents