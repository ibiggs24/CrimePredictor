from arcgis.geocoding import geocode
from arcgis.gis import GIS

gis = GIS()

def address_to_coords(address):
    try:
        location = geocode(address)[0]['location']
        return location['x'], location['y']
    except Exception as e:
        print("Geocoding failed:", e)
        return None
        