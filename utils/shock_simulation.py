def run_shock_simulation(user_input):

    # =========================
    # INPUTS
    # =========================
    tariff = user_input["tariff_percent"]
    export_restriction = user_input["export_restrictions"]
    disruption_level = user_input["supply_disruption_level"]
    currency_volatility = user_input["currency_volatility_percent"]
    base_margin = user_input["base_margin"]

    # Optional realism inputs
    import_cost_share = user_input.get("import_cost_share", 40) / 100
    dependency_ratio = user_input.get("dependency_ratio", 0.6)  # 0–1 scale
    industry_elasticity = user_input.get("industry_elasticity", "medium")

    # =========================
    # ELASTICITY FACTOR
    # =========================
    if industry_elasticity == "high":
        elasticity_factor = 1.0
    elif industry_elasticity == "low":
        elasticity_factor = 0.4
    else:
        elasticity_factor = 0.7  # medium default

    # =========================
    # TRADE SHOCK (Tariff Incidence Model)
    # =========================
    effective_tariff = tariff * dependency_ratio
    trade_shock = effective_tariff * elasticity_factor

    if export_restriction:
        trade_shock *= 1.3  # export bans amplify tariff impact

    # =========================
    # SUPPLY SHOCK
    # =========================
    if disruption_level == "high":
        supply_shock = 25
        supply_multiplier = 1.2
    elif disruption_level == "medium":
        supply_shock = 15
        supply_multiplier = 1.1
    else:
        supply_shock = 5
        supply_multiplier = 1.05

    # =========================
    # FINANCIAL SHOCK (Currency Pass-Through)
    # =========================
    exchange_pass_through = 0.75  # assume partial hedging
    currency_shock = (
        currency_volatility *
        import_cost_share *
        exchange_pass_through
    )

    # =========================
    # COMBINED BASE SHOCK SCORE
    # =========================
    base_shock_score = (
        (trade_shock * 0.5) +
        (supply_shock * 0.3) +
        (currency_shock * 0.2)
    )

    # =========================
    # NONLINEAR ESCALATION
    # =========================
    if base_shock_score > 50:
        base_shock_score *= 1.15  # crisis amplification

    # =========================
    # SHOCK MULTIPLIER EFFECT
    # =========================
    multiplier = 1 + ((supply_multiplier - 1) * 0.5)
    final_shock_score = base_shock_score * multiplier

    # =========================
    # MARGIN IMPACT
    # =========================
    margin_impact = final_shock_score * 0.35
    new_margin = base_margin - margin_impact

    # =========================
    # COST PRESSURE
    # =========================
    cost_pressure = (
        (effective_tariff * import_cost_share) +
        currency_shock
    )

    # =========================
    # RISK CLASSIFICATION
    # =========================
    if final_shock_score > 70:
        risk_classification = "Critical"
    elif final_shock_score > 50:
        risk_classification = "High"
    elif final_shock_score > 30:
        risk_classification = "Medium"
    else:
        risk_classification = "Low"

    # =========================
    # TRADE SHOCK LEVEL
    # =========================
    if trade_shock > 20:
        trade_shock_level = "High"
    elif trade_shock > 10:
        trade_shock_level = "Medium"
    else:
        trade_shock_level = "Low"

    return {
        "shock_level_score": round(final_shock_score, 2),
        "trade_shock_component": round(trade_shock, 2),
        "supply_shock_component": round(supply_shock, 2),
        "financial_shock_component": round(currency_shock, 2),
        "margin_impact_percent": round(margin_impact, 2),
        "new_margin": round(new_margin, 2),
        "cost_pressure_percent": round(cost_pressure, 2),
        "risk_classification": risk_classification,
        "currency_impact_percent": round(currency_shock, 2),
        "trade_shock_level": trade_shock_level,
        "profit_margin_compression_percent": round(margin_impact, 2)
    }