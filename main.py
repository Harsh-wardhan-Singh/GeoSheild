from utils.ai_model import run_ai_engine

def analyze_business(user_input):

    ai_output = run_ai_engine(user_input)

    # Safety clamp (no negative margin shown in UI)
    current_margin = max(0, round(ai_output["current_predicted_margin"], 2))
    optimized_margin = max(0, round(ai_output["optimized_predicted_margin"], 2))

    base_margin = user_input["base_margin"]

    profit_drop = round(base_margin - current_margin, 2)
    margin_recovery = round(ai_output["margin_recovery"], 2)

    # Risk messaging
    risk_level = ai_output["predicted_risk_level"]

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

    # Final structured output for Flask
    result = {
        "risk_analysis": {
            "risk_level": risk_level,
            "risk_message": risk_message
        },
        "profit_analysis": {
            "base_margin": base_margin,
            "current_predicted_margin": current_margin,
            "profit_drop": profit_drop
        },
        "optimization": {
            "optimal_dependency_allocation": ai_output["optimal_dependency_allocation"],
            "optimized_predicted_margin": optimized_margin,
            "margin_recovery": margin_recovery,
            "optimization_message": optimization_message
        }
    }

    return result


# Optional local test
if __name__ == "__main__":
    sample_input = {
        "dependencies": {
            "China": 75,
            "India": 10,
            "Vietnam": 15
        },
        "base_margin": 18,
        "import_cost_share": 40
    }
    sample_input_high = {
    "dependencies": {
        "China": 75,
        "India": 10,
        "Vietnam": 15
    },
    "base_margin": 20,
    "import_cost_share": 50
    }
    sample_input_low = {
    "dependencies": {
        "China": 20,
        "India": 40,
        "Vietnam": 40
    },
    "base_margin": 18,
    "import_cost_share": 30
    }

    print(analyze_business(sample_input))
    print(analyze_business(sample_input_high))
    print(analyze_business(sample_input_low))