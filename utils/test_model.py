from utils.master_model import run_full_analysis

def test_engine():

    sample_input = {
        "dependencies": {
            "China": 60,
            "India": 25,
            "Vietnam": 15
        },
        "base_margin": 18,
        "import_cost_share": 40
    }

    result = run_full_analysis(sample_input)

    assert result["simulation"]["new_margin"] <= sample_input["base_margin"]
    assert result["risk_level"] in ["Low", "Medium", "High", "Critical"]

    print("✅ Model Test Passed")
    print(result)


if __name__ == "__main__":
    test_engine()