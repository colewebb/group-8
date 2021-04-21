import React, { useState, useEffect }  from "react";
import reactDom from "react-dom";
import "./loggedout.css";
import logo from "../../assets/images/usu_logo_white.png";
import { Redirect, useLocation } from 'react-router'
import Menu from '../../navigation/menu';

export default function LoggedOut(props) {


  const handle_redirect = (e, data) => {
    e.preventDefault();

    };

  return (
    <div>
      <div className="root-container">
        <div className="card-login">
          <div className="card-top">
            <h2 className="card-login-title">You've been logged out</h2>
          </div>
          <div className="card-bottom">
          <form onSubmit={e => handle_redirect(e)}>
              <div className="input-field">
                <a href={"/login"} >Back to Login</a>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
//}
}
