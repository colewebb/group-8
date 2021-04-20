import React from "react";
import reactDom from "react-dom";
import "./breadcrumbs.css";

export default function Breadcrumbs(props) {
  return (
    <div className="breadcrumbs-view-root">
      <div className="breadcrumbs-sub-view">
       <h1 className="breadcrumbs-event-text">Men's Basketball</h1>
       <p className="breadcrumbs-location-text">Dee Glen Smith Spectrum</p>
       <p className="breadcrumbs-time-text">02/15/2021 - 7:00 PM</p>
      </div>
    </div>
  );
}
