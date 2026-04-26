def categorize(text):
    text = text.lower()

    if "it" in text or "software" in text:
        return "IT"
    elif "restaurant" in text or "horeca" in text:
        return "HORECA"
    elif "construct" in text:
        return "CONSTRUCTII"
    elif "persoane juridice" in text:
        return "JURIDIC"
    elif "persoane fizice" in text:
        return "PERSONAL"
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