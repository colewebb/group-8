import React, { useState, useEffect }  from "react";
import reactDom from "react-dom";
import "./account.styles.css";
import logo from "../../assets/images/usu_logo_white.png";
import { Redirect, useLocation } from 'react-router'
import Menu from '../../navigation/menu';


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

export default function Account(props) {
  const [submitted, setSubmitted] = useState(false);
  const [addBalance, setAddBalance] = useState('');
  const [balance, setBalance] = useState(localStorage.getItem('balance'));
  const [errorMessage, setErrorMessage] = useState(' ');


  function handleChangeBalance(e)  {
      e.preventDefault();

      setAddBalance(e.target.value);
    };

  const handleAddBalance = (e, data) => {
      e.preventDefault();
      setErrorMessage(' ');
      fetch(`http://localhost:8000/api/users/${localStorage.getItem('id')}/updatebalance/value=${addBalance}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `JWT ${localStorage.getItem('token')}`
        },
      })
        .then(res => res.json())
        .then(json => {
          if(json.balance){
            localStorage.setItem('balance', json.balance);
            setTimeout(() => {}, 2000);
            window.location = "/account";
          }else{
            setErrorMessage("Incorrect username or password");
          }
        },
        (error) => {
          setErrorMessage("Can't Connect.. Try again later");
        });
    };

  return (
    <div>
      <Menu />
      <h2 class="events-title-text">Account</h2>

      <div className="root-container">

        <div className="card-login">
          <div className="card-top">
            <h2 className="card-login-title">Add Balance</h2>
          </div>
          <div className="card-bottom">
            <h2 className="card-login-sub-title">Current: ${balance}</h2>
            <form onSubmit={e => handleAddBalance(e, {addBalance: addBalance})}>
              <div className="input-field">
                <input
                  type="text"
                  placeholder={"ex: 40"}
                  onChange={handleChangeBalance}
                  required
                />
              </div>
              <p className="error-message">{errorMessage}</p>
              <div className="input-field">
                <input className="input-submit" type="submit" value="Add" />
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
//}
}
