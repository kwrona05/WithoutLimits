import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Login from "./components/menu-components/Login";
import Profile from "./components/menu-components/UserData";
import HeartRate from "./components/menu-components/HeartData";
import Chart from "./components/menu-components/Charts";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/home" element={<Home />} />
        <Route path="/home/char" element={<Chart />} />
        <Route path="/home/profile" element={<Profile />} />
        <Route path="/home/heart-data" element={<HeartRate />} />
      </Routes>
    </Router>
  );
};
export default App;
