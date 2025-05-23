import numpy as np
from sklearn.base import BaseEstimator

def predict_single(model: BaseEstimator, hour: int, weekday: int, month: int, lat: float, lon: float):
    X = np.array([[hour, weekday, month, lat, lon]])
    prediction = model.predict(X)[0]
    prob = model.predict_proba(X)[0]
    confidence = np.max(prob)
    safety_score = round((1 - confidence) * 100, 2)
    return prediction, confidence, safety_score
    