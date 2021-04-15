import React, { useState, useEffect }  from "react";
import './menu.css';
import menuIcon from '../assets/images/menu_icon.png';

export default function Menu(props) {
  let [menuWidth, openMenu] = useState(0);

  const handle_logout = () => {
    localStorage.setItem('token', '');
    localStorage.setItem('username', '');
    window.location = "/login";
  }

  useEffect(() => {
    const { innerWidth: width} = window;
    console.log(width);
    if(width >= 720) {
      openMenu(menuWidth = 250);
    }
  });


  return (
    <nav>
      <div class="menuButton" onClick={() => openMenu(menuWidth = 250)}>
        <div className="menu-image-container">
          <img className="menu-icon" src={menuIcon} alt="Menu icon" />
        </div>
      </div>
      <div id="mySidenav" class="sidenav" style={{width: menuWidth}}>
        <div class="credits-container">
          <div class="credits-container-top">
            <h2 class="name-text">{`${localStorage.getItem('username')}`}</h2>
          </div>
          <h2 class="value-text">$34.00</h2>
          <h2 class="balance-text">Balance</h2>
          <div />
        </div>
        <div class="closebtn" href="" onClick={() => openMenu(menuWidth = 0)}>&times;</div>
        <a href="/account">Account</a>
        <a href="/events">Events</a>
        <a href="/reservations">Reservations</a>
        <a href="/faq">FAQ</a>
        <div class="logout-button-center">
          <div class="logout-button">
            <a class="logout-button-text" onClick={() => handle_logout()}>Logout</a>
          </div>
        </div>
      </div>
    </nav>
  );
}
