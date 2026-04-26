import requests
from bs4 import BeautifulSoup

URLS = [
    "https://monitoruloficial.ro/pierderi-persoane-fizice/",
    "https://monitoruloficial.ro/pierderi-persoane-juridice/",
    "https://monitoruloficial.ro/concursuri-posturi-publice/",
    "https://monitoruloficial.ro/anunturi-profesionisti/",
    "https://monitoruloficial.ro/publicare-acte-normative/"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def fetch_documents():
    documents = []

    for url in URLS:
        try:
            response = requests.get(url, headers=HEADERS)

            # 🔴 dacă e blocat, să știm
            if response.status_code != 200:
                print(f"ERROR {response.status_code} for {url}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            title = soup.title.string.strip() if soup.title else url

            documents.append({
                "title": title,
                "url": url
            })

        except Exception as e:
            print("SCRAPER ERROR:", e)

    return documents