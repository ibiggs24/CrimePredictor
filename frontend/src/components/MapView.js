import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

const redXIcon = new L.Icon({
  iconUrl: '/icons/red-x.png',
  iconSize: [25, 25],
  iconAnchor: [12, 12],
  popupAnchor: [0, -32]
});


function MapView({ coords, crimes }) {
  if (!coords) return null;
  return (
    <MapContainer center={coords} zoom={14} style={{ height: '400px', width: '100%' }}>
      <TileLayer
        attribution='&copy; OpenStreetMap contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {crimes.map((crime, idx) => (
        <Marker
          key={idx}
          position={[crime.Latitude, crime.Longitude]}
          icon={redXIcon}
        >
          <Popup>{crime["Primary Type"]}</Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}

export default MapView;