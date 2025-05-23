import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    # Extracts time/location from data
    df = df.copy()
    # Ensure proper datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df[df['Date'].notnull()]
    # Extract features
    df['hour'] = df['Date'].dt.hour
    df['weekday'] = df['Date'].dt.weekday
    df['month'] = df['Date'].dt.month
    # Remove rows with missing coordinates
    df = df[df['Latitude'].notnull() & df['Longitude'].notnull()]
    # Return features + target column
    return df[['hour', 'weekday', 'month', 'Latitude', 'Longitude', 'Primary Type']]