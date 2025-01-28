import { useNavigate } from "react-router-dom";
import SearchBar from "./menu-components/SearchBar";
import styles from "./Menu.module.scss";

const Menu = () => {
  const navigate = useNavigate();
  return (
    <div className={styles.menuContainer}>
      <div className={styles.buttonContainer}>
        <div
          className={styles.divBtn}
          onClick={() => {
            navigate("/home/heart-data");
          }}
        >
          Heart data
        </div>
        <div
          className={styles.divBtn}
          onClick={() => {
            navigate("/home/char");
          }}
        >
          Charts
        </div>
        <div
          className={styles.divBtn}
          onClick={() => {
            navigate("/home/profile");
          }}
        >
          Your profile
        </div>
      </div>
      <SearchBar />
    </div>
  );
};
export default Menu;
