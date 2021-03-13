import React from "react";
import reactDom from "react-dom";
import "./cart.styles.css";
import Menu from '../../navigation/menu';

export default function Cart(props) {
  return (
    <div>
      <Menu />
      <div>
       <h1>Cart</h1>
      </div>
    </div>
  );
}
