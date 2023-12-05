// App.js
import React, { useState, useEffect } from 'react';
import './App.css';
import CategoryBox from './checkboxes/CategoryBox.js';
import BackButton from './back_button/back_button.js';
import Map from './map/map.js';


function App() {
  const [categories, setCategories] = useState([]);
  const [selectedCategories, setSelectedCategories] = useState([]);

  useEffect(() => {
    // Fetch categories from the server
    fetch('http://localhost:3000/api/categories')
      .then(response => response.json())
      .then(data => setCategories(data))
      .catch(error => console.error('Error fetching categories:', error));
  }, []);

  const handleCheckboxChange = (category, isChecked) => {
    console.log('Handling checkbox change:', category, isChecked);

    if (isChecked) {
      setSelectedCategories((prevCategories) => [...prevCategories, category]);
    } else {
      setSelectedCategories((prevCategories) =>
        prevCategories.filter((selectedCategory) => selectedCategory !== category)
      );
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <BackButton />
      </header>

      <div className="checkboxesDiv">
        {categories.map((categoryData) => (
          <CategoryBox
            key={categoryData.id} // Use a unique key for each category
            id={categoryData.id.toLowerCase().replace(/\s+/g, '')}
            checkboxCategory={categoryData.label}
            onChange={(isChecked) => handleCheckboxChange(categoryData.label, isChecked)}
          />
        ))}
      </div>
      <div className="mapDiv">
        <Map selectedCategories={selectedCategories} />
      </div>
      <div className="footer">
        <p>Code 4 Girls!</p>
      </div>
    </div>
  );
}

export default App;
