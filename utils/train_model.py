import pandas as pd
import joblib
from sklearn.ensemble import GradientBoostingRegressor, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

df = pd.read_csv("data/training_data.csv")

X = df[[
    "china_risk", "india_risk", "vietnam_risk",
    "dep_china", "dep_india", "dep_vietnam",
    "import_cost_share",
    "base_margin"
]]

y_class = df["risk_level"]
y_reg = df["new_margin"]

# Classification model
classifier_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", RandomForestClassifier(n_estimators=200))
])

classifier_pipeline.fit(X, y_class)

# Regression model
regressor_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("reg", GradientBoostingRegressor())
])

regressor_pipeline.fit(X, y_reg)

joblib.dump(classifier_pipeline, "risk_classifier.pkl")
joblib.dump(regressor_pipeline, "profit_regressor.pkl")

print("Models trained and saved.")