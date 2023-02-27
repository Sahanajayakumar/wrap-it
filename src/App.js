import React, { useState } from 'react';
import './yt.css';

function YoutubeInput() {
  const [youtubeUrl, setYoutubeUrl] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
       await fetch('http://localhost:5000/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
        // body: JSON.stringify({ youtubeUrl })
      }).then(response => {
      if (response.ok) {
        console.log(response.json)
        console.log('YouTube URL submitted successfully');
        // <div className="App">
        response.json().then(body => {
          body.forEach((value, i) => {
            return <img key={i} src={value} alt="can't show image" />;
          })})    
   
      // </div>
      } else {
        console.error('Failed to submit YouTube URL');
      }
    })
    } catch (error) {
      console.error('Failed to submit YouTube URL:', error);
    }
  }

  const handleChange = (event) => {
    setYoutubeUrl(event.target.value);
  }

  return (
    <div className="form-wrapper">
      <form onSubmit={handleSubmit} className="form-container">
        <h1>Enter a YouTube URL</h1>
        <div className="form-group">
          <label htmlFor="youtubeUrl">YouTube URL:</label>
          <input
            type="text"
            id="youtubeUrl"
            name="youtubeUrl"
            value={youtubeUrl}
            onChange={handleChange}
            placeholder="https://www.youtube.com/watch?v=VIDEO_ID"
            required
          />
        </div>
        <div className="form-group">
          <button type="submit">Submit</button>
        </div>
      </form>
    </div>
  );
}

export default YoutubeInput;
