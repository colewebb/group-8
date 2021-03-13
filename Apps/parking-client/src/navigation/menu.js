import React, { useState, useEffect }  from "react";
import reactDom from "react-dom";
import { Link } from 'react-router-dom';
import './menu.css';
import menuIcon from '../assets/images/menu_icon.png';

export default function Menu(props) {

  let [menuWidth, openMenu] = useState(0);

  return (
    <nav>
      <div class="menuButton" onClick={() => openMenu(menuWidth = 250)}>
        <div className="menu-image-container">
          <img className="menu-icon" src={menuIcon} alt="Menu icon" />
        </div>
      </div>
      <div id="mySidenav" class="sidenav" style={{width: menuWidth}}>
        <a class="closebtn" onClick={() => openMenu(menuWidth = 0)}>&times;</a>
        <a href="/account">Account</a>
        <a href="/reservations">Reservations</a>
        <a href="/faq">FAQ</a>
        <a href="/login">Logout</a>
      </div>
    </nav>
  );
}
