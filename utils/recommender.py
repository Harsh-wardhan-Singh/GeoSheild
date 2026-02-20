import json

def recommend_alternatives(current_countries, risk_scores):
    meta = json.load(open("data/country_meta.json"))

    suggestions = []

    for country, data in meta.items():
        if country not in current_countries:
            score = (100 - risk_scores.get(country, 50)) + data["stability"] * 5
            suggestions.append((country, score))

    suggestions.sort(key=lambda x: x[1], reverse=True)

    return [country for country, _ in suggestions[:3]]