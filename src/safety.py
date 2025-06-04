# Objective crime weights (affects safety score)
CRIME_WEIGHTS = {
    "HOMICIDE": 10,
    "CRIMINAL SEXUAL ASSAULT": 9,
    "ROBBERY": 8,
    "AGGRAVATED ASSAULT": 7,
    "BATTERY": 6,
    "BURGLARY": 5,
    "MOTOR VEHICLE THEFT": 5,
    "THEFT": 4,
    "CRIMINAL DAMAGE": 3,
    "DECEPTIVE PRACTICE": 2,
    "NARCOTICS": 2,
    "OTHER OFFENSE": 1,
    "WEAPONS VIOLATION": 5,
    "ARSON": 6,
    "ASSAULT": 5
}


def compute_safety_score(crime_list, population):
    if not crime_list or not population:
        return 0
    weighted_total = 0
    for crime in crime_list:
        crime_type = str(crime["Primary Type"]) if "Primary Type" in crime else "OTHER OFFENSE"
        weight = CRIME_WEIGHTS.get(crime_type, 1)
        weighted_total += weight
    # Weighted incidents per 1k residents
    risk_ratio = (weighted_total / population) * 1000 
    # Cap on how bad crime gets
    max_risk = 2000
    # Sets final score between 0 and 100
    normalized = 1 - min(risk_ratio / max_risk, 1)
    score = round(normalized * 100, 2)
    return round(score, 2)
