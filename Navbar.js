import React from 'react';
import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark" style={{ backgroundColor: '#0d6efd' }}>
      <div className="container justify-content-center">
        <span className="navbar-brand fw-bold fs-4 me-5">SIGN SEEKER</span>
        <div className="d-flex">
          <Link className="nav-link text-white mx-3" to="/sign-to-translate">Sign to Translate</Link>
          <span className="text-white">|</span>
          <Link className="nav-link text-white mx-3" to="/translate-to-sign">Translate to Sign</Link>
        </div>
      </div>
    </nav>
  );
}
