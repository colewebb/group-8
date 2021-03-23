import React from "react";
import reactDom from "react-dom";
import "./eventCard.css";


export default function EventCard(props) {

  return (
    <div className="event-card-container">
      <div className="event-card">
        <div className="event-card-top">
          <h2 className="event-card-title-text">USU Mens Basketball</h2>
        </div>
        <p className="event-card-date-text">03/04/2021 - 7:00pm</p>
        <p className="event-card-location-text">Dee Glen Smith Spectrum</p>
        <a className="overlay" href="/lots">
          <a className="reserve-text" href="/lots">Reseve Now</a>
        </a>
      </div>
    </div>
  );
}
