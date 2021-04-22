import React from "react";
import reactDom from "react-dom";
import "./lotCard.css";
import Menu from '../../navigation/menu';
import smallIcon from '../../assets/icons/006-scooter.png';
import mediumIcon from '../../assets/icons/002-car.png';
import largeIcon from '../../assets/icons/049-camper.png';import Moment from 'moment';

export default function lotCard(props) {
  var path = `cart/${props.id}`

  console.log(props.capSmallActual)
  return (
    <div className="lot-card-root">
      <div className="lot-card-container">
        <div className="lot-card-sub-container">

        {props.capSmallActual > 0  ?
          <a className="lot-card-price-container" href={`${path}/?size=Small`}>
            <img className="lot-otions-icon-small" src={smallIcon} alt="rv icon" />
            <p className="lot-card-option-title-text">Small</p>
            <p className="lot-card-price-text">${props.costSmall}</p>
          </a>
        :
          <div />
        }
        {props.capMediumActual > 0  ?
          <a className="lot-card-price-container" href={`${path}/?size=Medium`}>
            <img className="lot-otions-icon" src={mediumIcon} alt="rv icon" />
            <p className="lot-card-option-title-text">Medium</p>
            <p className="lot-card-price-text">${props.costMedium}</p>
          </a>
        :
          <div />
        }
        {props.capLargeActual > 0  ?
          <a className="lot-card-price-container" href={`${path}/?size=Large`}>
            <img className="lot-otions-icon" src={largeIcon} alt="rv icon" />
            <p className="lot-card-option-title-text">Large</p>
            <p className="lot-card-price-text">${props.costLarge}</p>
          </a>
        :
          <div />
        }
        {props.capSmallActual < 0 && props.capLargeActual < 0 && props.capMediumActual < 0 ?
          <div className="lot-card-price-container">
            <p className="lot-card-option-title-text-sold-out">Sold Out</p>
            <div />
          </div>
        :
          <div />
        }
        </div>
        <div className="lot-card-info-container">
            <p className="lot-card-name-text">{props.name}</p>
            <div className="lot-card-info-row">
              <div>
                <p className="lot-card-info-text">{props.openTime}</p>
                <p className="lot-card-info-sub-text">Open Time</p>
              </div>
              <div>
                <p className="lot-card-info-text">{props.address}</p>
                <p className="lot-card-info-sub-text">Address</p>
              </div>
              <div>
                <p className="lot-card-info-text">0.03 miles</p>
                <p className="lot-card-info-sub-text">Distance</p>
              </div>
            </div>
        </div>
      </div>
    </div>
  );
}
