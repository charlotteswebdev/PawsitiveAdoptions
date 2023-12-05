// Map.js
import React, { useState, useEffect } from 'react';
import './map.css';
import osm from "./map_custom_tiler.js";
import 'leaflet/dist/leaflet.css';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import { Icon } from 'leaflet';
import MarkerClusterGroup from "react-leaflet-cluster";
import BookButton from '../BookButton.js';

function Map({ selectedCategories }) {
  const [filteredEvents, setFilteredEvents] = useState([]);

  useEffect(() => {
    if (selectedCategories.length > 0) {
      // Fetch events based on selected categories
      fetch(`http://localhost:3000/api/events?categories=${selectedCategories.join(',')}`)
        .then(response => response.json())
        .then(data => setFilteredEvents(data))
        .catch(error => console.error('Error fetching events:', error));
    } else {
      // No categories selected, clear the filtered events
      setFilteredEvents([]);
    }
  }, [selectedCategories]);

  const mapPinIcon = new Icon({
    iconUrl: "https://cdn-icons-png.flaticon.com/128/8944/8944264.png",
    iconSize: [50, 50]
  });

  return (
    <MapContainer center={[51.509204, -0.136817]} zoom={13} maxZoom={15}>
      <TileLayer url={osm.maptiler.url} attribution={osm.maptiler.attribution} />
      <MarkerClusterGroup chunkedLoading>
        {filteredEvents.map((event, index) => (
          <Marker key={index} position={[event.latitude, event.longitude]} icon={mapPinIcon}>
            <Popup>Event:{event.name}  <br/>Time:{event.event_time} <br/><BookButton/></Popup>
          </Marker>
        ))}
      </MarkerClusterGroup>
    </MapContainer>
  );
}

export default Map;
