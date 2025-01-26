import styles from "./SearchBar.module.scss";
const SearchBar = () => {
  return (
    <div className={styles.container}>
      <input placeholder="Enter the city" type="text" />
      <button type="submit">Search</button>
    </div>
  );
};
export default SearchBar;
