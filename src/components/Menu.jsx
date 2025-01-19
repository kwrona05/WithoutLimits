import { useNavigate } from "react-router-dom";
import SearchBar from "./menu-components/SearchBar";

const Menu = () => {
  return (
    <div className="menu-container">
      <div className="buttons-container">
        <div className="heart-data-btn" onClick={() => console.log("clicked")}>
          Heart data
        </div>
        <div
          className="historical-charts"
          onClick={() => console.log("clicked")}
        >
          Charts
        </div>
        <div className="place-check" onClick={() => console.log("clicked")}>
          Search place
        </div>
        <div className="user-data" onClick={() => console.log("clicked")}>
          Your profile
        </div>
      </div>
      <SearchBar />
    </div>
  );
};
export default Menu;
