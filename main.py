from src.load_data import load_crime_data
from src.features import engineer_features
from src.model import train_model
from src.predict import predict_single
from datetime import datetime

def main():
    df = load_crime_data("data/raw/crime_data_2025.csv")
    df_features = engineer_features(df)
    model = train_model(df_features)
    lat = float(input("Enter latitude: "))
    lon = float(input("Enter longitude: "))
    now = datetime.now()
    hour = now.hour
    weekday = now.weekday()
    month = now.month
    label, confidence, safety = predict_single(model, hour, weekday, month, lat, lon)
    print(f"\n Predicted Crime Type: {label}")
    print(f"\n Model Confidence: {round(confidence * 100, 2)}%")
    print(f"Safety Score: {safety}/100 (lower = higher risk)")
    
if __name__ == "__main__":
    main()