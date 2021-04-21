import React, { useState, useEffect } from 'react'
import reactDom from "react-dom";
import "./reservationCard.css";
import Moment from 'moment';



export default function ReservationCard(props) {
  const [address, setAddress] = useState('');
  const [name, setName] = useState('');
  const [startTime, setStartTime] = useState('');

  useEffect(() => {
    console.log('props');
    console.log(props);
    console.log('props');

    fetch(`http://localhost:8000/api/events/${props.eventId}/`, {
            headers: {
              Authorization: `JWT ${localStorage.getItem('token')}`
            }
          })
      .then(res => res.json())
      .then(
        (result) => {
          console.log(result);
          console.log(result.address);

          setAddress(result.address);
          setName(result.name);
          setStartTime(result.startTime);
        },
        (error) => {

        }
      )
  }, [])

  Moment.locale('en');
   var dt = startTime;
   var path = `reservation/${props.id}/`

  return (
    <div className="event-card-container">
    {props.eventId ?
        <div className="event-card">
          <div className="event-card-top">
            <h2 className="event-card-title-text">{name}</h2>
          </div>
          <div className="event-card-info-row">
            <div className="event-card-info">
              <p className="event-card-info-sub-text">Date:</p>
              <p className="event-card-date-text">{Moment(dt).format('MMMM Do YYYY, h:mm:ss a')}</p>
              <p className="event-card-info-sub-text">Location:</p>
              <p className="event-card-location-text">{address}</p>
            </div>
            <a className="event-card-info-action" href={path}>
              <div className="event-card-info-action-button">
                <p className="event-card-action-button-text">See Reservation</p>
              </div>
            </a>
          </div>
        </div>
      :
          <h2 className="event-card-no-text">You don't have any reservations</h2>
    }
    </div>
  );
}
