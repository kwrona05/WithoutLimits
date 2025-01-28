import { useRef } from "react";
import styles from "./SearchBar.module.scss";
const SearchBar = () => {
  const inputRef = useRef(null);

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(inputRef.current.value);
  };
  //In the future search has to navigate to the city
  return (
    <div className={styles.container}>
      <input ref={inputRef} placeholder="Enter the city" type="text" />
      <button type="submit" onClick={handleSubmit}>
        Search
      </button>
    </div>
  );
};
export default SearchBar;
