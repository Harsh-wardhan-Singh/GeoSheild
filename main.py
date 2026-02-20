from utils.ai_model import run_ai_engine
from utils.risk_engine import calculate_country_risk
from utils.vulnerability import calculate_vulnerability
from utils.simulator import simulate_shock
from utils.recommender import recommend_alternatives
from utils.shock_simulation import run_shock_simulation


def analyze_business(user_input):

    mode = user_input.get("mode", "ai")  

    if mode == "shock":

        shock_output = run_shock_simulation(user_input)

        return {
            "mode": "Shock Simulation",
            "shock_analysis": shock_output
        }


    ai_output = run_ai_engine(user_input)

    risk_level = ai_output.get("predicted_risk_level", "Unknown")
    risk_confidence = ai_output.get("risk_confidence", 0)

    current_margin = max(0, round(ai_output.get("current_predicted_margin", 0), 2))
    optimized_margin = max(0, round(ai_output.get("optimized_predicted_margin", 0), 2))

    base_margin = user_input.get("base_margin", 20)
    profit_drop = round(base_margin - current_margin, 2)
    margin_recovery = round(ai_output.get("margin_recovery", 0), 2)

    country_risk_scores = calculate_country_risk()

    vulnerability_breakdown, total_vulnerability = calculate_vulnerability(
        user_input.get("dependencies", {}),
        country_risk_scores
    )

    simulation_result = simulate_shock(
        tariff_factor=total_vulnerability,
        component_share=user_input.get("import_cost_share", 40),
        base_margin=base_margin
    )

    recommended_countries = recommend_alternatives()

    # Risk messaging
    if risk_level in ["High", "Critical"]:
        risk_message = "High geopolitical exposure detected."
    elif risk_level == "Medium":
        risk_message = "Moderate supply chain vulnerability."
    else:
        risk_message = "Supply chain currently stable."

    # Optimization message
    if margin_recovery > 0:
        optimization_message = (
            f"Reallocation could recover approximately {margin_recovery}% margin."
        )
    else:
        optimization_message = "Current allocation is already near optimal."

    result = {

        "mode": "AI Risk Prediction",

        "risk_analysis": {
            "risk_level": risk_level,
            "risk_confidence_percent": risk_confidence,
            "risk_message": risk_message,
            "country_risk_scores": country_risk_scores
        },

        "profit_analysis": {
            "base_margin": base_margin,
            "current_predicted_margin": current_margin,
            "profit_drop": profit_drop
        },

        "vulnerability_analysis": {
            "country_exposure": vulnerability_breakdown,
            "total_vulnerability_score": round(total_vulnerability, 2)
        },

        "simulation_analysis": simulation_result,

        "optimization": {
            "optimal_dependency_allocation": ai_output.get("optimal_dependency_allocation", {}),
            "optimized_predicted_margin": optimized_margin,
            "margin_recovery": margin_recovery,
            "optimization_message": optimization_message,
            "recommended_stable_countries": recommended_countries
        }
    }

    return result