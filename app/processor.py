def analyze(text):
    text_lower = text.lower()

    if any(word in text_lower for word in ["it", "software", "digital", "informatic"]):
        category = "IT"
    elif any(word in text_lower for word in ["restaurant", "hotel", "turism", "alimentatie"]):
        category = "HORECA"
    elif any(word in text_lower for word in ["construct", "autorizatie", "urbanism", "locuinta"]):
        category = "CONSTRUCTII"
    elif any(word in text_lower for word in ["pierdut", "anunt", "publicare", "declar"]):
        category = "ALTELE"
    else:
        category = "ALTELE"

    return {
        "summary": text[:200],
        "category": category,
        "impact": "mic"
    }
