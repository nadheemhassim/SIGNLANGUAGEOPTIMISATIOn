import React, { useState } from 'react';

export default function TranslateToSign() {
  const [input, setInput] = useState('');
  const [images, setImages] = useState([]);

  const fetchImages = () => {
    fetch(`http://localhost:5000/get_images?text=${input}`)
      .then(res => res.json())
      .then(data => setImages(data.images))
      .catch(error => console.error('Error fetching images:', error));
  };

  return (
    <div className="container card-container text-center">
      <h2 className="mb-4">Translate to Sign</h2>

      <div className="input-group mb-4 w-50 mx-auto">
        <input
          type="text"
          className="form-control"
          placeholder="Type letters like ABC"
          value={input}
          onChange={(e) => setInput(e.target.value.toUpperCase())}
        />
        <button className="btn btn-success" onClick={fetchImages}>Translate</button>
      </div>

      <div className="d-flex justify-content-center flex-wrap">
        {images.map((src, index) => (
          <img
            key={index}
            src={`http://localhost:5000${src}`}
            alt={`Sign ${index}`}
            className="m-2"
            style={{ height: '200px', borderRadius: '10px' }}
          />
        ))}
      </div>
    </div>
  );
}
