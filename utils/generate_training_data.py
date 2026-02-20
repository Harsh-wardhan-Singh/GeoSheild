import json
import pandas as pd
import random
import numpy as np

def load_trends():
    with open("data/risk_trends.json") as f:
        return json.load(f)

def generate_data(samples=1000):

    trends = load_trends()
    data = []

    for _ in range(samples):

        trend = random.choice(trends)

        china_risk = trend["China"]
        india_risk = trend["India"]
        vietnam_risk = trend["Vietnam"]

        dep_china = random.randint(20, 80)
        dep_india = random.randint(5, 50)
        dep_vietnam = 100 - dep_china - dep_india
        if dep_vietnam < 0:
            dep_vietnam = 0

        base_margin = random.uniform(10, 25)
        import_cost_share = random.uniform(20, 60)

        weighted_risk = (
            china_risk * dep_china +
            india_risk * dep_india +
            vietnam_risk * dep_vietnam
        ) / 100

        cost_shock = (weighted_risk / 100) * import_cost_share
        new_margin = base_margin - cost_shock

        if weighted_risk > 80:
            risk_level = "Critical"
        elif weighted_risk > 65:
            risk_level = "High"
        elif weighted_risk > 45:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        data.append([
            china_risk, india_risk, vietnam_risk,
            dep_china, dep_india, dep_vietnam,
            import_cost_share,
            base_margin,
            new_margin,
            risk_level
        ])

    df = pd.DataFrame(data, columns=[
        "china_risk", "india_risk", "vietnam_risk",
        "dep_china", "dep_india", "dep_vietnam",
        "import_cost_share",
        "base_margin",
        "new_margin",
        "risk_level"
    ])

    df.to_csv("data/training_data.csv", index=False)

if __name__ == "__main__":
    generate_data()