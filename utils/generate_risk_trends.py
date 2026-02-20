import json
from datetime import datetime, timedelta

def load_news():
    with open("data/news.json") as f:
        return json.load(f)

def generate_risk_trends():

    news = load_news()

    base_risk = {
        "China": 40,
        "India": 30,
        "Vietnam": 25
    }

    start_date = datetime(2025, 9, 1)
    trends = []

    for i in range(30): 

        current_date = start_date + timedelta(days=i * 10)

        # Increase risk if recent news exists
        for article in news:
            if article["country"] == "China":
                base_risk["China"] += article["severity"] * 0.1
            if article["country"] == "India":
                base_risk["India"] += article["severity"] * 0.1
            if article["country"] == "Vietnam":
                base_risk["Vietnam"] += article["severity"] * 0.1

        trends.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "China": round(base_risk["China"], 2),
            "India": round(base_risk["India"], 2),
            "Vietnam": round(base_risk["Vietnam"], 2)
        })

    with open("data/risk_trends.json", "w") as f:
        json.dump(trends, f, indent=2)

    print("Risk trends generated successfully.")

if __name__ == "__main__":
    generate_risk_trends()