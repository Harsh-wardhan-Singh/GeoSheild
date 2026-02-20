import json

def recommend_alternatives():

    with open("data/country_meta.json") as f:
        meta = json.load(f)

    scores = []

    for country, data in meta.items():
        score = (100 - data["base_risk"]) + (data["stability"] * 5)
        scores.append((country, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    return [country for country, _ in scores[:3]]