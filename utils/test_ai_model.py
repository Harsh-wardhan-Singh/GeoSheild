from utils.ai_model import run_ai_engine

test_input = {
    "dependencies": {
        "China": 75,
        "India": 10,
        "Vietnam": 15
    },
    "base_margin": 18,
    "import_cost_share": 40
}

result = run_ai_engine(test_input)

print(result)