import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar">
      <h1>Chord Analyzer</h1>
      <div className="links">
        <Link to="/">Chord</Link>
        <Link to="/other">Other page</Link>
      </div>
    </nav>
  );
};

export default Navbar;
