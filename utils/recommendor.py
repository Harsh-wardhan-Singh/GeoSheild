import json

def recommend_alternatives(excluded_country):
    with open("data/country_meta.json", "r") as f:
        country_data = json.load(f)

    recommendations = []

    for country, data in country_data.items():
        if country == excluded_country:
            continue

        risk = data["risk"]
        stability = data["stability"]

        score = (100 - risk) + stability * 5

        recommendations.append((country, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    top_3 = [country for country, _ in recommendations[:3]]

    return top_3