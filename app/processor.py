def categorize(text):
    text = text.lower()

    if "pierderi" in text:
        return "PIERDERI ACTE"

    elif "persoane fizice" in text:
        return "PERSOANE FIZICE"

    elif "persoane juridice" in text:
        return "PERSOANE JURIDICE"

    elif "concurs" in text or "posturi" in text:
        return "CONCURSURI"

    elif "acte normative" in text:
        return "ACTE NORMATIVE"

    else:
        return "ALTELE"


def summarize(text):
    return text[:120] + "..."


def analyze(doc):
    title = doc.get("title", "")

    return {
        "title": title,
        "category": categorize(title),
        "summary": summarize(title)
    }