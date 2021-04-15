import React, { useState, useEffect } from 'react'
import reactDom from "react-dom";
import "./reservation.css";
import Menu from '../../navigation/menu';
import Breadcrumbs from '../breadcrumbs/breadcrumbs';
import rvIcon from '../../assets/images/rv-icon.png';
import rvIconInactive from '../../assets/images/rv-icon-inactive.png';
import Map from '../map/map.js';
var QRCode = require('qrcode.react');

export default function Reservation(props) {
  const currentUrl = window.location.href;
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [reservation, setReservation] = useState([]);
  const [events, setEvents] = useState([]);
  const [lot, setLot] = useState([]);

  useEffect(() => {
    fetch(`http://localhost:8000/api/reservation/${getReservationId(currentUrl)}/`, {
            headers: {
              Authorization: `JWT ${localStorage.getItem('token')}`
            }
          })
      .then(res => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setReservation(result);
        },
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
      fetch(`http://localhost:8000/api/events/5/`)
        .then(res => res.json())
        .then(
          (result) => {
            setIsLoaded(true);
            setEvents(result);
          },
          (error) => {
            setIsLoaded(true);
            setError(error);
          }
        )
        fetch(`http://localhost:8000/api/lots/1/`)
          .then(res => res.json())
          .then(
            (result) => {
              setIsLoaded(true);
              setLot(result);
            },
            (error) => {
              setIsLoaded(true);
              setError(error);
            }
          )
  }, [])

  function getReservationId(url){
    let re = /(?<=reservation\/)(.*)(?=\/\?*)/i;
    return re.exec(url)[0];
  }


  return (
    <div>
      <Menu />
      <Breadcrumbs name={events.name} address={events.address} date={events.startTime}/>
      <div class="reservation-view-root">
          <div class="reservation-options-container">
            <p class="reservation-title-text">Your Reservation:</p>
            <div class="reservation-options-row">
              <div class="reservation-option-active">
                <QRCode value="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO" />
              </div>
            </div>
            <p class="reservation-title-sub-text">Show this QR code to the lot attendant</p>
          </div>
          <div class="reservation-details-container">

            <div class="reservation-details-divider" />
            <div class="reservation-details-row">
              <p class="reservation-details-text">Lot:</p>
              <p class="reservation-details-text">Spectrum South Lot</p>
            </div>
            <div class="reservation-details-row">
              <p class="reservation-details-text">Distance:</p>
              <p class="reservation-details-text">5 minutes walking</p>
            </div>
            <div class="reservation-details-row">
              <p class="reservation-details-text">Open:</p>
              <p class="reservation-details-text">6:00 PM</p>
            </div>
            <div class="reservation-details-divider" />
            <div><iframe  class="reservation-map-container" frameBorder="0" scrolling="no" marginHeight="0" marginWidth="0" src="https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q=Dee%20glem%20smith%20spectrum+(My%20Business%20Name)&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"></iframe></div>
            <div class="space-30" />
            <div class="reservation-details-divider" />
            <div>
              <p className="reservation-additional-info-text">This purchase is for parking only and does not include entry into the event.</p>
            </div>
          </div>
        </div>
    </div>
  );
}
