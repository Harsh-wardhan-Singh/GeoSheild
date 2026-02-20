from flask import Flask, jsonify, request
from flask_cors import CORS
import json, math

DEMO_MODE=True
app = Flask(__name__)
CORS(app)

# -------- RISK ENGINE --------

severity_weight={"High":5,"Medium":3,"Low":1}
policy_multiplier={"Export Ban":2.5,"Tariff":1.5,"Sanction":2,"Subsidy":-0.5,"Agreement":-1}

def recency_weight(days):
    return math.exp(-days/7)

def compute_risk(events):
    import math
    scores={}
    for e in events:
        sev={"High":5,"Medium":3,"Low":1}[e["severity"]]
        mult={"Export Ban":2.5,"Tariff":1.5,"Sanction":2,"Subsidy":-0.5,"Agreement":-1}[e["type"]]
        rec=math.exp(-e["days_ago"]/7)
        scores[e["country"]]=scores.get(e["country"],0)+sev*mult*rec
    max_score=max(scores.values()) if scores else 1
    return {c:round((s/max_score)*100) for c,s in scores.items()}

# -------- ROUTES --------

@app.route("/")
def home():
    return "Backend Running"

@app.route("/risk", methods=["POST"])
def risk():
    data=request.json or {}

    # fallback demo data
    events=data.get("events",[
        {"country":"China","type":"Export Ban","severity":"High","days_ago":1},
        {"country":"China","type":"Tariff","severity":"Medium","days_ago":3},
        {"country":"Vietnam","type":"Subsidy","severity":"Low","days_ago":2}
    ])

    return jsonify({"success":True,"data":compute_risk(events)})

@app.route("/vulnerability",methods=["POST"])
def vulnerability():

    data=request.json or {}

    deps=data.get("dependencies",{})
    events=data.get("events",[])

    risks=compute_risk(events)

    total=sum(percent*risks.get(country,0) for country,percent in deps.items())

    return jsonify({"success":True,"vulnerability_score":round(total/100)})

@app.route("/explain",methods=["POST"])
def explain():
    events=(request.json or {}).get("events",[])
    countries=set(e["country"] for e in events)

    return jsonify({
        "success":True,
        "explanation":{
            c:"Risk influenced by recent geopolitical policies affecting trade."
            for c in countries
        }
    })

@app.route("/health")
def health():
    return {"status":"ok"}

@app.route("/simulate",methods=["POST"])
def simulate():
    d=request.json or {}
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
    if DEMO_MODE:
        print("Running in demo mode with mock data.")
    app.run(debug=True,host="0.0.0.0")