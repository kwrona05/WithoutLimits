const SearchBar = () => {
  return (
    <div className="search-bar-container">
      <input className="search-bar" placeholder="Enter the city" type="text" />
      <button className="submit-search">Search</button>
    </div>
  );
};
export default SearchBar;
