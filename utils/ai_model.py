import joblib
import pandas as pd
import json

# Load trained models
classifier = joblib.load("models/risk_classifier.pkl")
regressor = joblib.load("models/profit_regressor.pkl")

# IMPORTANT:
# These MUST match the exact column order used in training
FEATURE_COLUMNS = [
    "china_risk", "india_risk", "vietnam_risk",
    "dep_china", "dep_india", "dep_vietnam",
    "import_cost_share",
    "base_margin"
]

def load_latest_risk():
    with open("data/risk_trends.json") as f:
        return json.load(f)[-1]

def build_feature_dataframe(user_input):
    trend = load_latest_risk()

    feature_dict = {
        "china_risk": trend["China"],
        "india_risk": trend["India"],
        "vietnam_risk": trend["Vietnam"],
        "dep_china": user_input["dependencies"]["China"],
        "dep_india": user_input["dependencies"]["India"],
        "dep_vietnam": user_input["dependencies"]["Vietnam"],
        "import_cost_share": user_input["import_cost_share"],
        "base_margin": user_input["base_margin"]
    }

    # Convert to DataFrame with correct column order
    return pd.DataFrame([feature_dict], columns=FEATURE_COLUMNS)

def predict_current_state(user_input):
    features_df = build_feature_dataframe(user_input)

    risk_prediction = classifier.predict(features_df)[0]
    risk_proba = classifier.predict_proba(features_df)[0]

    # Confidence = probability of predicted class
    class_index = list(classifier.classes_).index(risk_prediction)
    confidence = risk_proba[class_index]

    margin_prediction = regressor.predict(features_df)[0]

    return risk_prediction, float(margin_prediction), float(confidence)

def optimize_allocation(user_input):

    best_margin = -999
    best_allocation = None

    for china in range(30, 81, 10):
        for india in range(10, 51, 10):

            vietnam = 100 - china - india
            if vietnam < 0:
                continue

            candidate_input = {
                "dependencies": {
                    "China": china,
                    "India": india,
                    "Vietnam": vietnam
                },
                "base_margin": user_input["base_margin"],
                "import_cost_share": user_input["import_cost_share"]
            }

            _, predicted_margin = predict_current_state(candidate_input)

            if predicted_margin > best_margin:
                best_margin = predicted_margin
                best_allocation = candidate_input["dependencies"]

    return best_allocation, best_margin

def run_ai_engine(user_input):

    risk_level, predicted_margin, risk_confidence = predict_current_state(user_input)

    optimal_allocation, optimized_margin = optimize_allocation(user_input)

    margin_recovery = optimized_margin - predicted_margin

    return {
    "predicted_risk_level": risk_level,
    "risk_confidence": round(risk_confidence * 100, 2),
    "current_predicted_margin": round(predicted_margin, 2),
    "optimal_dependency_allocation": optimal_allocation,
    "optimized_predicted_margin": round(optimized_margin, 2),
    "margin_recovery": round(margin_recovery, 2)
    }