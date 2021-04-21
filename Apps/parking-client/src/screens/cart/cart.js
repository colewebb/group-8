import React, { useState, useEffect } from 'react'
import Steps from '../steps/steps';
import "./cart.styles.css";
import Menu from '../../navigation/menu';
import Breadcrumbs from '../breadcrumbs/breadcrumbs';
import smallIcon from '../../assets/icons/006-scooter.png';
import mediumIcon from '../../assets/icons/002-car.png';
import largeIcon from '../../assets/icons/049-camper.png';

import rvIconInactive from '../../assets/images/rv-icon-inactive.png';
import Map from '../map/map.js';

export default function Cart(props) {
  const currentUrl = window.location.href;
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);
  const [events, setEvents] = useState([]);
  const [size, setSize] = useState(getSpotSize(currentUrl));
  const [price, setPrice] = useState(items.costSmall);
  const [lot, setLot] = useState(items.costSmall);



  useEffect(() => {
    fetch(`http://localhost:8000/api/lots/${getLotId(currentUrl)}/`, {
            headers: {
              Authorization: `JWT ${localStorage.getItem('token')}`
            }
          })
      .then(res => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setItems(result);
          updateSize(getSpotSize(currentUrl));
          if(size == 'Small'){
            setPrice(result.costSmall);
          }else if(size == 'Medium'){
            setPrice(result.costMedium);
          }else if(size == 'Large'){
            setPrice(result.costLarge);
          }
        },
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
      fetch(`http://localhost:8000/api/events/${getEventId(currentUrl)}/`, {
              headers: {
                Authorization: `JWT ${localStorage.getItem('token')}`
              }
            })
        .then(res => res.json())
        .then(
          (result) => {
            setIsLoaded(true);
            setEvents(result);
          },
          (error) => {
            localStorage.setItem('token', '');
            localStorage.setItem('username', '');
            localStorage.setItem('id', '');
          }
        )
  }, [])

  function updateSize(size) {
    setSize(size);
    if(size == 'Small'){
      setPrice(items.costSmall);
    }else if(size == 'Medium'){
      setPrice(items.costMedium);
    }else if(size == 'Large'){
      setPrice(items.costLarge);
    }
  }

  function getLotId(url){
    let re = /(?<=cart\/)(.*)(?=\/\?size=*)/i;
    return re.exec(url)[0];
  }

  function getSpotSize(url){
    let re = /(?<=\?size=)(.*)/i;
    return re.exec(url)[0];
  }

  function getEventId(url){
    let re = /(?<=events\/)(.*)(?=\/lots*)/i;
    return re.exec(url)[0];
  }

  function purchase(data){
    console.log('data');
    console.log(JSON.stringify(data));
    console.log('data');

    fetch('http://localhost:8000/api/reservations/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `JWT ${localStorage.getItem('token')}`
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(json => {
        if(json.id){
          window.location = `/reservation/${json.id}/`;
        }
      },
      (error) => {
        localStorage.setItem('token', '');
        localStorage.setItem('username', '');
        localStorage.setItem('id', '');
        window.location = "/loggedout";
      });
    }


  return (
    <div class="cart-view-root-1">
      <Menu />
      <Steps step={3}/>
      <Breadcrumbs name={events.name} address={events.address} date={events.startTime}/>
      <div class="cart-view-root">
          <div class="cart-options-container">
            <div class="cart-options-row">
            {items.capSmallActual < items.capSmallMax  ?
              <div class={`cart-option${size == 'Small' ? "-active" : ""}`} onClick={() => updateSize("Small")}>
                <img className={`cart-options-icon-small${size == 'Small' ? "-active" : ""}`} src={smallIcon} alt="rv icon" />
                <p class={`cart-option-title-text${size == 'Small' ? "-active" : ""}`}>Small</p>
                <p class={`cart-option-price-text${size == 'Small' ? "-active" : ""}`}>${items.costSmall}</p>
              </div>
            :
            <div />
            }
            {items.capMediumActual < items.capMediumMax  ?
              <div class={`cart-option${size == 'Medium' ? "-active" : ""}`} onClick={() => updateSize("Medium")}>
                <img className={`cart-options-icon-medium${size == 'Medium' ? "-active" : ""}`} src={mediumIcon} alt="rv icon" />
                <p class={`cart-option-title-text${size == 'Medium' ? "-active" : ""}`}>Medium</p>
                <p class={`cart-option-price-text${size == 'Medium' ? "-active" : ""}`}>${items.costMedium}</p>
              </div>
            :
            <div />
            }
            {items.capLargeActual < items.capLargeMax  ?
              <div class={`cart-option${size == 'Large' ? "-active" : ""}`} onClick={() => updateSize("Large")}>
                <img className={`cart-options-icon-large${size == 'Large' ? "-active" : ""}`} src={largeIcon} alt="rv icon" />
                <p class={`cart-option-title-text${size == 'Large' ? "-active" : ""}`}>Large</p>
                <p class={`cart-option-price-text${size == 'Large' ? "-active" : ""}`}>${items.costLarge}</p>
              </div>
            :
            <div />
            }
            </div>
          </div>
          <div class="cart-details-container">
            <div class="cart-details-divider" />
            <div class="cart-details-row">
              <p class="cart-details-text">Lot:</p>
              <p class="cart-details-text">{items.name}</p>
            </div>
            <div class="cart-details-row">
              <p class="cart-details-text">Distance:</p>
              <p class="cart-details-text">5 minutes walking</p>
            </div>
            <div class="cart-details-row">
              <p class="cart-details-text">Open:</p>
              <p class="cart-details-text">{items.openTime} PM</p>
            </div>
            <div class="cart-details-divider" />
            <div><iframe  class="cart-map-container" frameBorder="0" scrolling="no" marginHeight="0" marginWidth="0" src="https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q=Utah%20State%20University+(My%20Business%20Name)&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"></iframe></div>
            <div class="space-30" />
            <div class="cart-details-divider" />
            <div class="cart-details-row">
              <p class="cart-details-text">{size} Parking Spot</p>
              <p class="cart-details-text">1X</p>
            </div>
            <div class="cart-details-row">
              <p class="cart-total-text">TOTAL</p>
              <p class="cart-total-text">${price}</p>
            </div>
            <div class="cart-purchase-button-container" onClick={() => purchase({event: getEventId(currentUrl), lot: getLotId(currentUrl), size: size.toLowerCase()})}>
              <div class="cart-purchase-button">
                <div class="cart-purchase-button-text">Purchase</div>
              </div>
            </div>
            <div>
              <p className="cart-additional-info-text">This purchase is for parking only and does not include entry into the event.</p>
            </div>
          </div>
        </div>
    </div>
  );
}
