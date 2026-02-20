import random

def simulate_shock(tariff_factor, component_share, base_margin):

    cost_increase = tariff_factor * (component_share / 100)

    volatility = random.uniform(-1, 1)

    margin_drop = cost_increase + volatility

    new_margin = base_margin - margin_drop

    return {
        "cost_increase": round(cost_increase, 2),
        "margin_drop": round(margin_drop, 2),
        "new_margin": round(new_margin, 2)
    }