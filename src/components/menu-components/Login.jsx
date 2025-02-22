import React, { useRef, useState } from "react";
import Webcam from "react-webcam";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import styles from "./Login.module.scss";

const LoginRegister = () => {
  const navigate = useNavigate();
  const webcamRef = useRef(null);
  const [username, setUsername] = useState("");
  const [mode, setMode] = useState("login");
  const [message, setMessage] = useState("");

  const captureImage = () => {
    const imageSrc = webcamRef.current.getScreenshot();
    return dataURItoBlob(imageSrc);
  };

  const dataURItoBlob = (dataURI) => {
    const [header, data] = dataURI.split(",");
    const mimeString = header.match(/:(.*?);/)[1];
    const byteString = atob(data);
    const intArray = Uint8Array.from(byteString, (char) => char.charCodeAt(0));
    return new Blob([intArray], { type: mimeString });
  };

  const handleSubmit = async () => {
    const imageBlob = captureImage();
    const formData = new FormData();
    formData.append("file", imageBlob);

    if (mode === "register") {
      formData.append("username", username);
      try {
        console.log("something");
        const response = await axios.post(
          "http://localhost:8000/register",
          formData,
          { headers: { "Content-type": "multipart/form-data" } }
        );
        setMessage(response.data.image);

        navigate("/home");
      } catch (error) {
        console.error(error);
        setMessage(error.response?.data?.detail || "Registration Failed");
      }
    } else if (mode === "login") {
      try {
        const response = await axios.post(
          "http://localhost:8000/login",
          formData,
          { headers: { "Content-type": "multipart/form-data" } }
        );
        setMessage(response.data.message);
        navigate("/home");
      } catch (error) {
        setMessage(error.response?.data?.detail || "Login Failed");
      }
    }
  };

  return (
    <div className={styles.loginForm}>
      <h1>{mode === "login" ? "Login" : "Register"}</h1>
      {mode === "register" && (
        <input
          type="text"
          placeholder="Enter your username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      )}
      <div className={styles.webcamContainer}>
        <Webcam
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          onUserMediaError={(err) => {
            console.error("Webcam error:", err);
            setMessage("Webcam not found");
          }}
          videoConstraints={{
            facingMode: "user",
          }}
        />
      </div>
      <button
        onClick={handleSubmit}
        className={`${styles.loginButton} ${styles.actionButton}`}
      >
        {mode === "login" ? "Login" : "Register"}
      </button>
      <button
        className={`${styles.switchButton} ${styles.actionButton}`}
        onClick={() => setMode(mode === "login" ? "register" : "login")}
      >
        Switch to {mode === "login" ? "Register" : "Login"}
      </button>
      <p>{message}</p> {/*In the future add allerts*/}
    </div>
  );
};
export default LoginRegister;
