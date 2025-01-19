import Menu from "./Menu";
import Map from "./Map";

const Home = () => {
  return (
    <div className="container">
      <div className="menu-container">
        <Menu />
      </div>
      <div className="map-container">
        <Map />
      </div>
    </div>
  );
  //Mapa
  //Bar do dodawania lub oznaczania jako nieaktualne nowych miejsc
};
export default Home;
