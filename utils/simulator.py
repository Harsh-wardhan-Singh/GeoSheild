import numpy as np

def simulate_shock(total_exposure, base_margin, import_cost_share):

    # Shock proportional to exposure and cost share
    cost_increase = (total_exposure / 100) * import_cost_share

    new_margin = base_margin - cost_increase

    return {
        "cost_increase_percent": round(cost_increase, 2),
        "old_margin": base_margin,
        "new_margin": round(new_margin, 2),
        "margin_drop": round(base_margin - new_margin, 2)
    }