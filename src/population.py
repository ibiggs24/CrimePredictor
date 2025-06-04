import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from geopy.distance import geodesic
import math

# Load block group population CSV
population_df = pd.read_csv("blockgroup_population_2020.csv")

blockgroup_pop = {
    row["GEO_ID"].split("US")[-1]: int(row["P1_001N"])
    for _, row in population_df.iterrows()
}

# Load block group shapefile
blockgroup_gdf = gpd.read_file("../data/tl_2020_17_bg/tl_2020_17_bg.shp")
blockgroup_gdf = blockgroup_gdf.to_crs(epsg=4326)

def estimate_population(lat, lon, radius):
    try:
        center = (lat, lon)
        radius_km = radius / 1000.0
        estimated_pop = 0
        for _, row in blockgroup_gdf.iterrows():
            geoid = row["GEOID"]
            polygon = row.geometry
            centroid = polygon.centroid
            dist_km = geodesic(center, (centroid.y, centroid.x)).km
            pop = blockgroup_pop.get(geoid, 0)
            # Apply weight based on distance
            if dist_km <= radius_km * 1.5:
                weight = max(0.0, 1 - (dist_km / radius_km) ** 2)
                estimated_pop += pop * weight
        adjusted_population = int(estimated_pop * (1 + math.log1p(radius / 500)))
        return adjusted_population
    except Exception as e:
        print(f"[!] Population estimation failed: {e}")
        return None
