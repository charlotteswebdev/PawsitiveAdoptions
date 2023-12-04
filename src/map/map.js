// https://www.youtube.com/watch?v=jD6813wGdBA


import './map.css';
import osm from "./map_custom_tiler.js"; // map tiles ()

import 'leaflet/dist/leaflet.css'; // map css
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'; // map container, tilelayer (map images) and markers (map pins)
import { Icon } from 'leaflet'; // icon for map pins 
import MarkerClusterGroup from "react-leaflet-cluster";


function Map(){


    // writing as if these markers are coming from an api
    const mapPin = [
        {
            geocode: [51.5, -0.09],
            popUp: "Ice Skating"
        },
        {
            geocode: [51.53, -0.11],
            popUp: "Stocking Sewing"
        }
    ] 



    // map pin icon can be imported png into project !
    const mapPinIcon = new Icon({
        iconUrl: "https://cdn-icons-png.flaticon.com/128/8944/8944264.png", // current icon from flaticon.com
        iconSize: [50, 50] // pixel size of icon
    })



    return (
        <MapContainer center={[51.509204, -0.136817]} zoom={13}>
            <TileLayer url = {osm.maptiler.url} attribution = {osm.maptiler.attribution} />

            <MarkerClusterGroup chunkedLoading>
                {mapPin.map(marker => (
                <Marker position={marker.geocode} icon={mapPinIcon}>
                    <Popup> {marker.popUp} </Popup>
                </Marker>
                ))}
                </MarkerClusterGroup>

        </MapContainer>
    )
}

export default Map;