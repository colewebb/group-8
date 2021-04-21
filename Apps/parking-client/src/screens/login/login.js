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
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState(' ');


  function handleChangeUsername(e)  {
      e.preventDefault();

      setUsername(e.target.value);
    };

    function handleChangePassword(e)  {
        e.preventDefault();

        setPassword(e.target.value);
      };

  const handle_login = (e, data) => {
      e.preventDefault();
      setErrorMessage(' ');
      fetch('http://localhost:8000/token-auth/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
        .then(res => res.json())
        .then(json => {
          if(json.token){
            localStorage.setItem('token', json.token);
            localStorage.setItem('username', json.user.username);
            localStorage.setItem('id', json.user.id);
            window.location = "/";
          }else{
            setErrorMessage("Incorrect username or password");
          }
        },
        (error) => {
          setErrorMessage("Can't Connect.. Try again later");
        });
    };

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
          <form onSubmit={e => handle_login(e, {username: username, password: password})}>
            <div className="input-field">
              <input
                type="text"
                placeholder={"Username"}
                onChange={handleChangeUsername}
                required
              />
            </div>
            <div className="input-field">
              <input
                type="password"
                placeholder={"Password"}
                onChange={handleChangePassword}
                required
              />
            </div>
            <p className="error-message">{errorMessage}</p>
            <div className="input-field">
              <input className="input-submit" type="submit" value="Login" />
            </div>
            <div className="forgot-password-container">
              <a href={"/register"} className="forgot-password">Don't have an account: REGESTER HERE!</a>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
//}
}
