import { useState, useEffect } from "react";
import axios from "axios";

const HeartRate = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:8000/heartrate");
        setData(response.data);
      } catch (error) {
        console.error("Error while fetching heart rate data:", error);
      }
    };

    const interval = setInterval(fetchData, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="hear-data-container">
      <h2>Heart rate monitor</h2>
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
          {/*set colors to status*/}
        </div>
      ) : (
        <p>Loading...</p> /*Loading animation*/
      )}
    </div>
  );
};

export default HeartRate;
