from flask import Flask, render_template, request, jsonify
from main import analyze_business

app = Flask(__name__)

# =====================================
# Render Home Page
# =====================================
@app.route("/")
def home():
    return render_template("index.html")


# =====================================
# API Endpoint
# =====================================
@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    try:
        result = analyze_business(data)
        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)