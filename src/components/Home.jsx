import Menu from "./Menu";
import Map from "./Map";
import styles from "./Home.module.scss";

const Home = () => {
  return (
    <div className={styles.container}>
      <div className={styles.menuContainer}>
        <Menu />
      </div>
      <div className={styles.mapContainer}>
        <Map />
      </div>
    </div>
  );
};
export default Home;
