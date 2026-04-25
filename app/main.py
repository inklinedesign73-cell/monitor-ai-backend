from fastapi import FastAPI
from .database import engine, SessionLocal
from .models import Base, Document

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"status": "merge"}

@app.get("/documents")
def get_documents():
    db = SessionLocal()
    docs = db.query(Document).all()
    return docs

@app.get("/add-test")
def add_test():
    db = SessionLocal()

    doc = Document(
        title="Test Monitor Oficial",
        summary="Acesta este un test",
        category="IT"
    )

    db.add(doc)
    db.commit()

    return {"status": "added"}

from app.scraper import fetch_documents

@app.get("/scrape")
def scrape():
    docs = fetch_documents()
    return docs

from app.scraper import fetch_documents
from app.models import Document
from app.database import SessionLocal
from app.processor import analyze


@app.get("/ingest")
def ingest():
    db = SessionLocal()
    docs = fetch_documents()

    saved = 0

    for doc in docs:
        # verificăm dacă există deja
        exists = db.query(Document).filter(
            Document.title == doc["title"]
        ).first()

        if exists:
            continue

        # AI safe (merge și fără API key)
        try:
            ai_result = analyze(doc["title"])
        except Exception:
            ai_result = {
                "summary": "AI error / fallback",
                "category": "ALTELE",
                "impact": "mic"
            }

        # normalizăm dacă vine string din AI
        summary_text = ai_result if isinstance(ai_result, str) else ai_result.get("summary", "")

        category_text = ai_result.get("category", "ALTELE") if isinstance(ai_result, dict) else "ALTELE"

        new_doc = Document(
            title=doc["title"],
            summary=summary_text,
            category=category_text
        )

        db.add(new_doc)
        saved += 1

    db.commit()
    db.close()

    return {
        "status": "ok",
        "saved": saved
    }

