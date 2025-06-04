from src.geocode import address_to_coords
from src.spatial_query import find_nearby_crimes
from src.safety import compute_safety_score
from src.population import estimate_population
from collections import Counter

def main():
    print("=== Chicago Crime Location Checker ===")
    address = input("Enter your address within Chicago (don't include city and state): ").strip()
    try:
        distance = int(input("Enter search radius in meters (e.g. 500 or 1000): ").strip())
    except ValueError:
        print("Invalid radius. Defaulting to 1000 meters.")
        distance = 1000
    address += " Chicago, IL"
    coords = address_to_coords(address)
    if not coords:
        print("Could not find coordinates for that address.")
        return
    x, y = coords
    print(f"\nCoordinates: ({y:.5f}, {x:.5f})\n")
    print(f"Searching for nearby crimes in 2025 within {distance} meters...\n")
    crimes = find_nearby_crimes(x, y, distance=distance)
    if crimes:
        type_counts = Counter()
        for crime in crimes:
            crime_type = crime.get('Primary Type', 'Unknown')
            type_counts[crime_type] += 1
        print(f"Found {sum(type_counts.values())} nearby crimes:\n")
        for crime_type, count in type_counts.most_common():
            print(f"- {crime_type}: {count}")
        # Population estimate and safety score
        population = estimate_population(y, x, distance/2)
        score = compute_safety_score(crimes, population)
        print(f"\nEstimated Population: {population if population else 'Unknown'}")
        print(f"Safety Score: {score}/100 (lower = more risk)\n")
    else:
        print("No nearby crimes found.")

if __name__ == "__main__":
    main()
