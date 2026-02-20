import requests
import json
from datetime import datetime

API_KEY = ""  

NEWS_URL = "https://newsapi.org/v2/everything"

KEYWORDS = "tariff OR export ban OR trade restriction OR sanctions"

def fetch_news():
    params = {
        "q": KEYWORDS,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }

    response = requests.get(NEWS_URL, params=params)
    data = response.json()

    formatted_articles = []

    for article in data.get("articles", []):
        title = article["title"]

        # Basic classification logic
        if "China" in title:
            country = "China"
        elif "India" in title:
            country = "India"
        elif "Vietnam" in title:
            country = "Vietnam"
        else:
            continue

        if "tariff" in title.lower():
            event_type = "Tariff"
            severity = 4
        elif "sanction" in title.lower():
            event_type = "Sanctions"
            severity = 5
        elif "export" in title.lower():
            event_type = "Export Restriction"
            severity = 4
        else:
            event_type = "Trade Policy"
            severity = 2

        formatted_articles.append({
            "title": title,
            "country": country,
            "industry": "general",
            "event_type": event_type,
            "severity": severity,
            "date": article["publishedAt"][:10]
        })

    with open("data/news.json", "w") as f:
        json.dump(formatted_articles, f, indent=2)

    print("News data saved successfully.")

if __name__ == "__main__":
    fetch_news()