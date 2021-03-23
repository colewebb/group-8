import React, { useState, useEffect }  from "react";
import reactDom from "react-dom";
import "./login.styles.css";
import logo from "../../assets/images/usu_logo_white.png";
import { Redirect, useLocation } from 'react-router'


const useInput = initialValue => {
  const [value, setValue] = useState(initialValue)
  return {
    value,
    setValue,
    reset: () => setValue(''),
    bind: {
      value,
      onChange: event => {setValue(event.target.value)}
    }
  }
}

export default function Login(props) {
  const [submitted, setSubmitted] = useState(false);
    const {value: content, bind: bindContent, reset: resetContent} = useInput('')

    const handleSubmit = (event) => {
      event.preventDefault()
        setSubmitted(true)
    }
    if (submitted) {
      return <Redirect push to={{
        pathname: '/',
      }}
      />
    }

  return (
    <div className="root-container">
      <div className="card-login">
        <div className="card-top">
          <div className="image-container">
            <img className="login_image" src={logo} alt="Utah State logo" />
          </div>
          <h2 className="card-login-title">Event Parking</h2>
        </div>
        <div className="card-bottom">
          <h2 className="card-login-sub-title">Welcome Back!</h2>
          <form onSubmit={handleSubmit}>
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
