import { useNavigate } from "react-router-dom";
import SearchBar from "./menu-components/SearchBar";
import styles from "./Menu.module.scss";

const Menu = () => {
  return (
    <div className={styles.menuContainer}>
      <div className={styles.buttonContainer}>
        <div className={styles.divBtn} onClick={() => console.log("clicked")}>
          Heart data
        </div>
        <div className={styles.divBtn} onClick={() => console.log("clicked")}>
          Charts
        </div>
        <div
          className={styles.searchBar}
          onClick={() => console.log("clicked")}
        >
          Search place
        </div>
        <div className={styles.divBtn} onClick={() => console.log("clicked")}>
          Your profile
        </div>
      </div>
      <SearchBar />
    </div>
  );
};
export default Menu;
