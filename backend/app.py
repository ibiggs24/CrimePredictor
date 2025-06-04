import sys
import os
# Adds parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from flask_cors import CORS
from src.geocode import address_to_coords
from src.spatial_query import find_nearby_crimes
from src.safety import compute_safety_score
from src.population import estimate_population
from collections import Counter

app = Flask(__name__)
CORS(app)

@app.route("/check_crime", methods=["POST"])
def check_crime():
    data = request.get_json()
    address = data.get("address")
    address += " Chicago, IL"
    # Defaults distance to 1000 meters if not provided
    distance = int(data.get("radius", 1000))
    # Convert address to coordinates
    coords = address_to_coords(address)
    if not coords:
        return jsonify({"error": "Could not geocode address"}), 400
    lon, lat = coords  # Unpack coords
    crimes = find_nearby_crimes(lon, lat, distance)
    crime_counts = Counter(crime["Primary Type"] if "Primary Type" in crime else "Unknown" for crime in crimes)
    population = estimate_population(lat, lon, distance)
    safety_score = compute_safety_score(crimes, population)
    # Formats crimes for map display only holding onto essential fields
    simplified_crimes = []
    for c in crimes:
        try:
            simplified_crimes.append({
                "Primary Type": c["Primary Type"],
                "Latitude": float(c["Latitude"]),
                "Longitude": float(c["Longitude"])
        })
        except (KeyError, TypeError, ValueError):
            continue
    # Returns all data as JSON
    return jsonify({
        "lat": lat,
        "lon": lon,
        "safety_score": safety_score,
        "population": population,
        "crime_counts": dict(crime_counts),
        "crimes": simplified_crimes
    })

if __name__ == "__main__":
    app.run(debug=True)
