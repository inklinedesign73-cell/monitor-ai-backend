import os

USE_AI = True if os.getenv("OPENAI_API_KEY") else False

def analyze(text):
    """
    MVP SAFE:
    - dacă AI nu e configurat → fallback simplu
    - dacă e configurat → OpenAI
    """

    if not USE_AI:
        return {
            "summary": "AI dezactivat (fără API key)",
            "category": "ALTELE",
            "impact": "mic"
        }

    from openai import OpenAI

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
Extrage informații din text legislativ:

Returnează STRICT în format:
REZUMAT: ...
CATEGORIE: IT / HORECA / CONSTRUCTII / ALTELE
IMPACT: mic / mediu / mare

Text:
{text[:3000]}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content

    # parsing simplu (MVP)
    return result
