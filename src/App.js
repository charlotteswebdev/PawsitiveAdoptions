import './App.css';
import CategoryBox from './checkboxes/checkbox.js';
import BackButton from './back_button/back_button.js';
import Map from './map/map.js';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <BackButton/>
      </header>
      <body>
        <div className='checkbokesDiv'>
          < CategoryBox id="romantic" checkboxCategory="Romantic"/>
          < CategoryBox id="familyfriendly" checkboxCategory="Family friendly"/>
          < CategoryBox id="adventurous" checkboxCategory="Adventurous"/>
          < CategoryBox id="foodie" checkboxCategory="Foodie"/>
          < CategoryBox id="artsCrafts" checkboxCategory="Arts & Crafts"/>
          < CategoryBox id="music" checkboxCategory="Music"/>
        </div>
        <div className='mapDiv'>
          <Map/>
        </div>
        <div className='footer'>
          <p> Code 4 Girls !</p>
        </div>
      </body>
    </div>
  );
}

// <img src={logo} className="App-logo" alt="logo" />

export default App;
