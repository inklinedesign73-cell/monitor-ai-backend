from fastapi import FastAPI
from .database import engine, SessionLocal
from .models import Base, Document

from app.scraper import fetch_documents
from app.processor import analyze

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"status": "merge"}


@app.get("/documents")
def get_documents():
    db = SessionLocal()
    docs = db.query(Document).all()
    db.close()
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
    db.close()

    return {"status": "added"}


@app.get("/scrape")
def scrape():
    docs = fetch_documents()
    return docs


# 🔥 RESET DB (IMPORTANT)
@app.get("/reset")
def reset():
    db = SessionLocal()
    db.query(Document).delete()
    db.commit()
    db.close()
    return {"status": "reset done"}


# 🔥 INGEST CORECT
@app.get("/ingest")
def ingest():
    db = SessionLocal()
    docs = fetch_documents()

    saved = 0

    for doc in docs:
        exists = db.query(Document).filter(
            Document.title == doc["title"]
        ).first()

        if exists:
            continue

        try:
            ai_result = analyze({"title": doc["title"]})
        except Exception as e:
            print("ANALYZE ERROR:", e)
            ai_result = {
                "title": doc["title"],
                "summary": doc["title"][:100],
                "category": "ALTELE"
            }

        new_doc = Document(
            title=ai_result.get("title", doc["title"]),
            summary=ai_result.get("summary", ""),
            category=ai_result.get("category", "ALTELE")
        )

        db.add(new_doc)
        saved += 1

    db.commit()
    db.close()

    return {
        "status": "ok",
        "saved": saved
    }