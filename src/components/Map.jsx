import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import styles from "./Map.module.scss";

import markerIcon2x from "leaflet/dist/images/marker-icon-2x.png";
import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";

L.Icon.Default.mergeOptions({
  iconRetinaUrl: markerIcon2x,
  iconUrl: markerIcon,
  shadowUrl: markerShadow,
});

const Map = () => {
  const [places, setPlaces] = useState([]);

  // useEffect(() => {
  //   fetch("/api/places")
  //     .then((response) => response.json())
  //     .then((data) => setPlaces(data))
  //     .catch((error) => console.error("Cannot load place:", error));
  // }, []);

  // const position = { userPlace };

  return (
    <div className={styles.mapContainer}>
      <MapContainer
        center={[52.2297, 21.0122]}
        zoom={13}
        style={{ height: "600px", width: "100%" }}
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {/* {places.map((place, index) => (
        <Marker key={index} position={[place.latitude, place.longitude]}>
          <Popup>{place.name}</Popup>
        </Marker>
      ))} */}
      </MapContainer>
    </div>
  );
};

export default Map;
