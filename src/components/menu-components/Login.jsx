import React, { useRef, useState } from "react";
import Webcam from "react-webcam";
import axios from "axios";
import { useNavigate } from "react-router-dom";

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
    const byteString = atob(dataURI.split(",")[1]);
    const mimeString = dataURI.split(",")[0].split(":")[1].split(";")[0];
    const arrayBuffer = new ArrayBuffer(byteString.length);
    const intArray = new Uint8Array(arrayBuffer);

    for (let i = 0; i < byteString.length; i++) {
      intArray[i] = byteString.charCodeAt(i);
    }
    return new Blob([arrayBuffer], { type: mimeString });
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
        const response = await axios.post("/login", formData);
        setMessage(response.data.message);
        navigate("/home");
      } catch (error) {
        setMessage(error.response?.data?.detail || "Login Failed");
      }
    }
  };

  return (
    <div className="login-form">
      <h1>{mode === "login" ? "Login" : "Register"}</h1>
      {mode === "register" && (
        <input
          type="text"
          placeholder="Enter your username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      )}
      <Webcam ref={webcamRef} screenshotFormat="image/jpeg" />
      <button onClick={handleSubmit}>
        {mode === "login" ? "Login" : "Register"}
      </button>
      <button onClick={() => setMode(mode === "login" ? "register" : "login")}>
        Switch to {mode === "login" ? "Login" : "Register"}
      </button>
      <p>{message}</p> {/*In the future add allerts*/}
    </div>
  );
};
export default LoginRegister;
