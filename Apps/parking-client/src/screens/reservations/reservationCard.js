import React from "react";
import reactDom from "react-dom";
import "./reservationCard.css";
import Moment from 'moment';



export default function ReservationCard(props) {

  Moment.locale('en');
   var dt = props.startTime;
   var path = `reservation/${props.id}/`

  return (
    <div className="event-card-container">
      <div className="event-card">
        <div className="event-card-top">
          <h2 className="event-card-title-text">{props.name}</h2>
        </div>
        <div className="event-card-info-row">
          <div className="event-card-info">
            <p className="event-card-info-sub-text">Date:</p>
            <p className="event-card-date-text">{Moment(dt).format('MMMM Do YYYY, h:mm:ss a')}</p>
            <p className="event-card-info-sub-text">Location:</p>
            <p className="event-card-location-text">{props.address}</p>
          </div>
          <a className="event-card-info-action" href={path}>
            <div className="event-card-info-action-button">
              <p className="event-card-action-button-text">See Reservation</p>
            </div>
          </a>
        </div>
      </div>
    </div>
  );
}
