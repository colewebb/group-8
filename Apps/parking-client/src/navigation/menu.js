import React, { useState, useEffect }  from "react";
import './menu.css';
import menuIcon from '../assets/images/menu_icon.png';
import logo from "../assets/images/usu_logo_white.png";

export default function Menu(props) {
  let [menuWidth, openMenu] = useState(0);
  let [username, setUsername] = useState(localStorage.getItem('username'));
  let [balance, setBalance] = useState(localStorage.getItem('balance'));

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

    fetch(`http://localhost:8000/api/users/${localStorage.getItem('id')}/`, {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`
        }
      })
      .then(res => res.json())
      .then(
        (result) => {
          setBalance(result.balance);
          localStorage.setItem('balance', result.balance);
        },
        (error) => {
        }
      )
  }, [])



  return (
    <nav>
      <div class="menuButton" onClick={() => openMenu(menuWidth = 250)}>
        <div className="menu-image-container">
          <img className="menu-icon" src={menuIcon} alt="Menu icon" />
        </div>
      </div>
      <div id="mySidenav" class="sidenav" style={{width: menuWidth}}>
        <div className="image-container-menu">
          <img className="login_image" src={logo} alt="Utah State logo" />
        </div>
        <h2 className="card-login-title-menu">Event Parking</h2>
        <div class="credits-container">
          <div class="credits-container-top">
            <h2 class="name-text">{username}</h2>
          </div>
          <h2 class="value-text">${balance}</h2>
          <h2 class="balance-text">Balance</h2>
          <div />
        </div>
        <div class="closebtn" href="" onClick={() => openMenu(menuWidth = 0)}>&times;</div>
        <a href="/account">Account</a>
        <a href="/events">Events</a>
        <a href="/reservations">Reservations</a>
        <div class="logout-button-center">
          <div class="logout-button">
            <a class="logout-button-text" onClick={() => handle_logout()}>Logout</a>
          </div>
        </div>
      </div>
    </nav>
  );
}
