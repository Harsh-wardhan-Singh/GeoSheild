from utils.risk_engine import calculate_country_risk
from utils.vulnerability import calculate_vulnerability
from utils.simulator import simulate_shock
from utils.recommender import recommend_alternatives

RISK_THRESHOLD = 65

def run_full_analysis(user_input):

    risk_scores = calculate_country_risk()

    vulnerability = calculate_vulnerability(
        user_input["dependencies"],
        risk_scores
    )

    simulation = simulate_shock(
        vulnerability["total_exposure_score"],
        user_input["base_margin"],
        user_input["import_cost_share"]
    )

    max_country_risk = max(
        [risk_scores.get(c, 0) for c in user_input["dependencies"]]
    )

    risk_level = "Low"

    if max_country_risk > 80:
        risk_level = "Critical"
    elif max_country_risk > 65:
        risk_level = "High"
    elif max_country_risk > 45:
        risk_level = "Medium"

    recommendations = []

    if max_country_risk > RISK_THRESHOLD:
        recommendations = recommend_alternatives(
            user_input["dependencies"],
            risk_scores
        )

    return {
        "risk_scores": risk_scores,
        "vulnerability": vulnerability,
        "simulation": simulation,
        "risk_level": risk_level,
        "recommendations": recommendations
    }