import React, { useState, useEffect }  from "react";
import reactDom from "react-dom";
import Menu from '../../navigation/menu';
import "./events.styles.css";

export default function Events(props) {
  return (
    <div>
      <Menu />
      <div>
        <h1>Events</h1>
      </div>
    </div>
  );
}
