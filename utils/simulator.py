import random

def simulate_shock(tariff, component_share, base_cost, margin):
    """
    tariff = 20  (percent)
    component_share = 50  (percent of cost from that country)
    base_cost = 100
    margin = 20  (percent)
    """

    # Cost increase due to tariff
    tariff_impact = (tariff / 100) * (component_share / 100) * base_cost

    # Add small volatility (optional demo realism)
    volatility = random.uniform(-0.02, 0.02) * base_cost

    new_cost = base_cost + tariff_impact + volatility

    old_margin_value = base_cost * (margin / 100)
    new_margin_value = (base_cost + old_margin_value) - new_cost

    new_margin_percent = (new_margin_value / new_cost) * 100

    return {
        "old_margin_percent": margin,
        "new_margin_percent": round(new_margin_percent, 2),
        "cost_change": round(new_cost - base_cost, 2)
    }