import React from "react";
import reactDom from "react-dom";
import "./login.styles.css";
import logo from "../assets/images/usu_logo_white.png";

export default function Login(props) {
  return (
    <div className="root-container">
      <div className="card-login">
        <div className="card-top">
          <div className="image-container">
            <img src={logo} alt="Utah State logo" />
          </div>
          <h2 className="card-login-title">Event Parking</h2>
        </div>
        <div className="card-bottom">
          <h2 className="card-login-sub-title">Welcome Back!</h2>

          <form>
            <div className="input-field">
              <input
                type="text"
                placeholder={"Email"}
              />
            </div>
            <div className="input-field">
              <input
                type="password"
                placeholder={"Password"}
              />
            </div>
            <div className="forgot-password-container">
              <a href={"www.google.com"} className="forgot-password">Forgot Password?</a>
            </div>
            <div className="input-field">
              <input className="input-submit" type="submit" value="Login" />
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
