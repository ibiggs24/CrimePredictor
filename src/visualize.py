# Geospatial joins, filtering, feature creations

import folium

def plot_hotspots(df):
    m = folium.Map(location=[41.8781, -87.6298], zoom_start=11)
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=3,
            color='red',
            fill=True,
            fill_opacity=0.5
        ).add_to(m)
    m.save("outputs/crime_map.html")