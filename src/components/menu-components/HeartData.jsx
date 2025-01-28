import { useState, useEffect } from "react";
import axios from "axios";

const HeartRate = () => {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null); // Przechowywanie błędu

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:8001/heartrates");
        console.log("Fetched data:", response.data);
        setData(response.data); // Oczekiwane dane jako lista
        setError(null); // Zresetuj błąd po udanym pobraniu danych
      } catch (error) {
        console.error("Error while fetching heart rate data:", error);
        setError(
          "Error while fetching heart rate data. Please try again later."
        );
      }
    };

    const interval = setInterval(fetchData, 5000); // Co 5 sekund
    fetchData(); // Pobierz dane przy pierwszym załadowaniu komponentu
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="heart-data-container">
      <h2>Heart rate monitor</h2>
      {error && <p className="error-message">{error}</p>}{" "}
      {/* Wyświetlenie błędu */}
      {data && data.length > 0 ? (
        data.map((item, index) => (
          <div key={index} className="data-container">
            <p>
              <strong>Timestamp:</strong> {item.timestamp}
            </p>
            <p>
              <strong>Heart rate:</strong> {item.heart_rate}
            </p>
            <p>
              <strong>Status:</strong> {item.status}
            </p>
          </div>
        ))
      ) : error ? null : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default HeartRate;
