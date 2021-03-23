import React from "react";
import reactDom from "react-dom";
import "./breadcrumbs.css";

export default function Breadcrumbs(props) {
  return (
    <div class="breadcrumbs-view-root">
      <div class="breadcrumbs-sub-view">
       <h1 class="breadcrumbs-event-text">Men's Basketball</h1>
       <p class="breadcrumbs-location-text">Dee Glen Smith Spectrum</p>
       <p class="breadcrumbs-time-text">02/15/2021 - 7:00 PM</p>
      </div>
    </div>
  );
}
