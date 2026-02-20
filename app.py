from flask import Flask, jsonify, request
from flask_cors import CORS
import json, math

app = Flask(__name__)
CORS(app)

# -------- RISK ENGINE --------

severity_weight={"High":5,"Medium":3,"Low":1}
policy_multiplier={"Export Ban":2.5,"Tariff":1.5,"Sanction":2,"Subsidy":-0.5,"Agreement":-1}

def recency_weight(days):
    return math.exp(-days/7)

def compute_risk():
    with open("data/news.json") as f:
        events=json.load(f)

    scores={}
    for e in events:
        score=severity_weight[e["severity"]]*policy_multiplier[e["type"]]*recency_weight(e["days_ago"])
        scores[e["country"]]=scores.get(e["country"],0)+score

    max_score=max(scores.values()) if scores else 1
    return {c:round((s/max_score)*100) for c,s in scores.items()}

# -------- ROUTES --------

@app.route("/")
def home():
    return "Backend Running"

@app.route("/risk")
def risk():
    return jsonify(compute_risk())

@app.route("/vulnerability",methods=["POST"])
def vulnerability():
    deps=request.json
    risks=compute_risk()
    total=sum(percent*risks.get(country,0) for country,percent in deps.items())
    return jsonify({"vulnerability_score":round(total/100)})

@app.route("/simulate",methods=["POST"])
def simulate():
    d=request.json
    component_cost=d["base_cost"]*d["component_share"]/100
    increase=component_cost*d["tariff"]/100
    new_cost=d["base_cost"]+increase
    new_margin=((d["base_cost"]*(d["margin"]/100))-increase)/new_cost*100
    return jsonify({"old_margin":d["margin"],"new_margin":round(new_margin,2),"cost_increase":round(increase,2)})

@app.route("/recommend")
def recommend():
    return jsonify([
        {"country":"Vietnam","score":85},
        {"country":"India","score":78},
        {"country":"Mexico","score":72}
    ])

# -------- RUN SERVER --------

if __name__=="__main__":
    app.run(debug=True)