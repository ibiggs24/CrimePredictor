import pandas as pd
from math import radians, cos, sin, sqrt, atan2

crime_df = pd.read_csv("crime_data_2025.csv")

# Calculates distance between user locaton (lat1, lon1) and each crime (lat2, lon2)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Earth radius in meters
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def find_nearby_crimes(user_lon, user_lat, distance):
    crimes = []
    # Iterates through all crimes in DataFrame
    for _, row in crime_df.iterrows():
        try:
            crime_lat = float(row["Latitude"])
            crime_lon = float(row["Longitude"])
        except:
            continue
        # Calculates distance betweeen crime and user location
        d = haversine(user_lat, user_lon, crime_lat, crime_lon)
        if d <= distance:  # Guarantees its within users given distance
            crimes.append(row)
    return crimes

def get_citywide_crime_count():
    return len(crime_df)