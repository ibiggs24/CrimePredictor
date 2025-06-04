import { useState } from 'react';
import axios from 'axios';

// Handles user input
function SearchBar({ onResults }) {
  const [address, setAddress] = useState('');
  const [radius, setRadius] = useState('1000');
  // Submit form data to backend and pass result to parent
  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post('http://127.0.0.1:5000/check_crime', {
      address,
      radius: parseInt(radius)
    });
    onResults(res.data);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        placeholder="Address (only street + number)"
        value={address}
        onChange={e => setAddress(e.target.value)}  // Updates address
      />
      <input
        type="number"
        placeholder="Radius (m)"
        value={radius}
        onChange={e => setRadius(e.target.value)}  // Updates radius
      />
      <button type="submit">Search</button>
    </form>
  );
}

export default SearchBar;
