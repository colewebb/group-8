import React from "react";
import reactDom from "react-dom";
import { Link } from 'react-router-dom';
import './nav.styles.css';

export default function Nav(props) {
  const navStyle = {
    color: 'white'
  }

  return (
    <nav>
      <h3>LOGO</h3>
      <ul className="nav-links">
        <Link style={navStyle} to='/menu'>
          <li>Menu</li>
        </Link>
        <Link style={navStyle} to='/login'>
          <li>Logout</li>
        </Link>
      </ul>
    </nav>
  );
}
