import React from "react";
import reactDom from "react-dom";
import "./account.styles.css";
import Menu from '../../navigation/menu';

export default function Account(props) {
  return (
    <div>
      <Menu />
      <div>
        <h1>Account</h1>
      </div>
    </div>
  );
}
