import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './Navbar';
import TranslateToSign from './pages/TranslateToSign';
import SignToTranslate from './pages/SignToTranslate';
import './App.css';


function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<SignToTranslate />} />
        <Route path="/sign-to-translate" element={<SignToTranslate />} />
        <Route path="/translate-to-sign" element={<TranslateToSign />} />
      </Routes>
    </Router>
  );
}

export default App;
