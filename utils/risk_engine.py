import json
from collections import defaultdict

SEVERITY_MULTIPLIER = 8
MAX_RISK = 100

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def calculate_country_risk():
    news = load_json("data/news.json")
    meta = load_json("data/country_meta.json")

    risk = defaultdict(int)

    # Base risk from country meta
    for country in meta:
        risk[country] = meta[country]["base_risk"]

    # Add news severity impact
    for article in news:
        country = article["country"]
        severity = article["severity"]
        risk[country] += severity * SEVERITY_MULTIPLIER

    # Cap risk
    for country in risk:
        risk[country] = min(risk[country], MAX_RISK)

    return dict(risk)