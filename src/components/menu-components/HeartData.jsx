import { useState, useEffect } from "react";
import axios from "axios";

const HeartRate = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null); // Przechowywanie błędu

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:8001/heartrates");
        setData(response.data);
        setError(null); // Zresetuj błąd po udanym pobraniu danych
      } catch (error) {
        console.error("Error while fetching heart rate data:", error);
        setError(
          "Error while fetching heart rate data. Please try again later."
        );
      }
    };

    const interval = setInterval(fetchData, 5000); // Co 5 sekund
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="hear-data-container">
      <h2>Heart rate monitor</h2>
      {error && <p className="error-message">{error}</p>}{" "}
      {/* Wyświetlenie błędu */}
      {data ? (
        <div className="data-container">
          <p>
            <strong>Timestamp:</strong> {data.timestamp}
          </p>
          <p>
            <strong>Heart rate:</strong> {data.heart_rate}
          </p>
          <p>
            <strong>Status:</strong> {data.status}
          </p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default HeartRate;
