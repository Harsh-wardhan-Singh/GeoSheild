def calculate_vulnerability(dependency_dict, risk_scores):
    """
    dependency_dict = {"China": 60, "Vietnam": 30}
    risk_scores = {"China": 75, "Vietnam": 35}
    """

    total_exposure = 0

    for country, dependency in dependency_dict.items():
        country_risk = risk_scores.get(country, 0)

        exposure = (dependency / 100) * country_risk
        total_exposure += exposure

    return round(total_exposure, 2)