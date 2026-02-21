# 🌍 GeoShield – AI-Powered Geopolitical Risk Intelligence Platform

![Website Preview](assets/website_preview.png)

🔗 **Live Right Now:** https://your-geoshield-app.onrender.com/  
*(Click above to simulate real-time global trade risk scenarios!)*

---

## 📌 Overview

**GeoShield** is a full-stack AI-driven web platform designed to analyze **geopolitical supply chain risk, trade shocks, and profit margin vulnerability** for global businesses.

The system operates in **two powerful modes**:

- **AI Risk Prediction Mode** – Machine Learning-based risk & margin forecasting  
- **Shock Simulation Mode** – Interactive macroeconomic disruption engine  

This project demonstrates a complete **end-to-end intelligent risk modeling pipeline**:

📌 Risk modeling → ML inference → Economic simulation → Optimization → Interactive dashboard → Cloud deployment  

It combines:

- **Machine Learning** (Scikit-Learn)
- **Macroeconomic shock modeling**
- **Vulnerability scoring**
- **Flask backend**
- **HTML/CSS/JavaScript frontend**
- **Static geopolitical risk visualization**
- **Cloud deployment** (Render.com)

---

## 🎯 Motivation

Modern global supply chains face increasing exposure to:

- Tariff escalations  
- Trade wars  
- Export restrictions  
- Supply chain disruptions  
- Currency volatility  
- Geopolitical instability  

Businesses often lack quantitative tools to measure:

- Margin compression risk  
- Country exposure vulnerability  
- Trade shock impact  
- Allocation optimization opportunities  

GeoShield was built to:

- Quantify geopolitical exposure  
- Model trade shock scenarios  
- Predict margin vulnerability  
- Provide optimization insights  
- Serve as a real-world example of ML-powered economic intelligence  

---

## 🏗️ Architecture

```
                   ┌────────────────┐
                   │   Web Browser  │
                   │  (User Inputs) │
                   └───────▲────────┘
                           │
                    JSON POST Request
                           │
                   ┌───────▼────────┐
                   │   Flask API    │
                   │ analyze_business() 
                   └───────▲────────┘
                           │
          ┌────────────────┴────────────────┐
          │                                 │
   AI Risk Prediction Mode         Shock Simulation Mode
          │                                 │
  ML Margin Forecasting            Macroeconomic Shock Engine
          │                                 │
  Vulnerability Analysis           Trade + Supply + Currency
          │                                 │
  Optimization Engine              Risk Classification
          │                                 │
          └───────────────┬─────────────────┘
                          ▼
                 Structured JSON Output
                          ▼
                  Interactive Dashboard
```


---

## ⚙️ Core System Modes

---

# 🤖 Mode 1 – AI Risk Prediction

This mode uses a trained ML model to evaluate:

- Predicted Risk Level (Low / Medium / High / Critical)
- Risk Confidence %
- Predicted Current Margin
- Profit Drop Estimation
- Vulnerability Score
- Optimized Allocation Suggestion
- Margin Recovery Potential

### 🔍 How It Works

User inputs:

- Country dependency distribution  
- Base profit margin  
- Import cost share  

Backend computes:

1. Country risk scoring  
2. Weighted vulnerability exposure  
3. ML-based margin prediction  
4. Profit drop calculation  
5. Optimization-based reallocation  

---

# ⚡ Mode 2 – Trade Shock Simulation Engine

This interactive mode simulates macroeconomic disruption scenarios.

Users control:

- Tariff (%)  
- Export Restrictions  
- Supply Disruption Level  
- Currency Volatility (%)  
- Dependency Ratio  
- Industry Elasticity  

### 🧠 Economic Components Modeled

The simulation engine models:

- Trade shock impact  
- Supply chain amplification  
- Currency risk pressure  
- Cost inflation effect  
- Margin compression  
- Risk classification  

### 📊 Shock Output Metrics

- Shock Level Score  
- Trade Shock Classification  
- Margin Impact %  
- New Predicted Margin  
- Cost Pressure %  
- Currency Impact %  
- Overall Risk Classification  

---

## 📈 Static Risk Trend Visualization

GeoShield includes a **static geopolitical risk trend graph** powered by `risk_trends.json`.

This frontend feature provides:

- Historical risk index trends per country  
- Comparative visualization  
- Contextual macro-risk analysis  

The graph dynamically renders country-specific risk movement, giving users visual insight alongside predictive modeling.

---

## 🗂️ Full Code Structure

```text
project_root
├── app.py # Flask entry point
├── main.py # Core orchestration logic
├── requirements.txt # Production dependencies
├── runtime.txt # Python version config
├── model.pkl # Pre-trained ML model
├── risktrends.json # Static risk trend dataset
├── utils/
│ ├── ai_model.py
│ ├── risk_engine.py
│ ├── vulnerability.py
│ ├── simulator.py
│ ├── shock_simulation.py
│ └── recommender.py
├── templates/
│ └── index.html
├── static/
│ ├── script.js
│ ├── style.css
└── README.md
```

---

## 🛠️ Installation (Local Development)

Clone Repository

```bash
git clone https://github.com/yourusername/geoshield.git
cd geoshield
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Locally

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

🚀 Deployment (Render.com)

GeoShield is deployed using Render with:

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**
```bash
gunicorn app:app
```

The trained model (model.pkl) is already included in the repository, so no retraining is required after deployment.

## 🧪 Example Scenario

**Input:**
```text
AI Model:
China: 60%
Vietnam: 25%
India: 15%
Base Margin: 20%
Import Cost Share: 40%

Shock Simulation:
Tariff: 15%
Export Ban: Enabled
Supply Disruption: High
Currency Volatility: 8%
```
**Output:**
```text
Shock Level: 67.4
Risk Classification: High
Margin Impact: -5.2%
New Margin: 14.8%
Cost Pressure: 6.1%
```
## Future Improvements

- Real-time geopolitical risk API integration
- Live currency feeds
- Monte Carlo simulation modeling
- Industry-specific calibration
- Dynamic trend auto-updating
- Advanced ML / Deep Learning forecasting using TensorFlow

## 📬 Contact

Created by Harsh Wardhan Singh, Shikhar Sadhu and Sn Omm Tripathi.
For collaborations please dm us!

## 🌍 Live Demo

Visit: https://your-geoshield-app.onrender.com/

Simulate your own supply chain risk scenarios today!

⭐ If you found this project interesting, consider starring the repository!
