import React, { useEffect, useState } from 'react';

export default function SignToTranslate() {
  const [prediction, setPrediction] = useState('');

  useEffect(() => {
    const interval = setInterval(() => {
      fetch('http://localhost:5000/prediction')
        .then(res => res.json())
        .then(data => setPrediction(data.prediction))
        .catch(err => console.error('Prediction fetch error:', err));
    }, 500);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="container card-container text-center">
      <h2 className="mb-4">Sign to Translate</h2>

      <img
        src="http://localhost:5000/video"
        alt="Webcam"
        width="800"
        className="rounded border border-primary"
      />

      <h3 className="mt-4 text-success">{prediction}</h3>
    </div>
  );
}
