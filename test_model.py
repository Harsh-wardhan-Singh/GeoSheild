import json
from utils.vulnerabilities import calculate_vulnerability
from utils.simulator import simulate_shock
from utils.recommendor import recommend_alternatives


def load_country_risk():
    with open("data/country_meta.json", "r") as f:
        data = json.load(f)

    # Extract only risk scores
    risk_scores = {country: info["risk"] for country, info in data.items()}
    return risk_scores


def test_vulnerability():
    print("\n===== TESTING VULNERABILITY ENGINE =====")

    dependency = {
        "China": 60,
        "Vietnam": 30
    }

    risk_scores = load_country_risk()

    score = calculate_vulnerability(dependency, risk_scores)

    print("Dependency:", dependency)
    print("Risk Scores:", risk_scores)
    print("Total Exposure Score:", score)


def test_simulator():
    print("\n===== TESTING SHOCK SIMULATOR =====")

    result = simulate_shock(
        tariff=20,           # 20% tariff
        component_share=50,  # 50% cost from affected country
        base_cost=100,       # Base production cost
        margin=20            # 20% margin
    )

    print("Simulation Result:")
    print(result)


def test_recommender():
    print("\n===== TESTING RECOMMENDATION ENGINE =====")

    recommendations = recommend_alternatives("China")

    print("Top 3 Alternative Countries:")
    print(recommendations)


if __name__ == "__main__":
    test_vulnerability()
    test_simulator()
    test_recommender()