import json
from collections import defaultdict

def calculate_country_risk():

    with open("data/news.json") as f:
        news = json.load(f)

    risk_scores = defaultdict(float)

    for article in news:
        country = article["country"]
        severity = article["severity"]

        risk_scores[country] += severity * 2  # weight factor

    # Normalize risk scores
    for country in risk_scores:
        risk_scores[country] = round(min(100, risk_scores[country]), 2)

    return risk_scores