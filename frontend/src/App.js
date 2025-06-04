import { useState } from 'react';
import SearchBar from './components/SearchBar';
import MapView from './components/MapView';
import './App.css';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="App">
      <h1 className="App-header">Chicago Neighborhood Crime Checker 2025</h1>
      <SearchBar onResults={setResult} />
      {result && (
        <div>
          <p>Total Crime Count: {Object.values(result.crime_counts).reduce((sum, count) => sum + count, 0)}</p>
          <p>Estimated Population: {result.population}</p>
          <p>Safety Score: {result.safety_score}</p>
          <h3>Crime Breakdown:</h3>
          <ul>
            {Object.entries(result.crime_counts)
            .sort((a, b) => b[1] - a[1]) // Sort descending by count
            .map(([type, count]) => (
                <li key={type}>{type}: {count}</li>
            ))}
          </ul>

          {/* Displays interactive crime map */}
          <MapView coords={[result.lat, result.lon]} crimes={result.crimes} />
        </div>
      )}
    </div>
  );
}

export default App;
