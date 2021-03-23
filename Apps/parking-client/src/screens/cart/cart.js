import React from "react";
import reactDom from "react-dom";
import "./cart.styles.css";
import Menu from '../../navigation/menu';
import Breadcrumbs from '../breadcrumbs/breadcrumbs';
import rvIcon from '../../assets/images/rv-icon.png';
import rvIconInactive from '../../assets/images/rv-icon-inactive.png';
import Map from '../map/map.js';

export default function Cart(props) {
  return (
    <div>
      <Menu />
      <Breadcrumbs />
      <div className="cart-view-root">
          <div className="cart-options-container">
            <div className="cart-options-row">
              <div className="cart-option-active">
                <img className="cart-otions-icon" src={rvIcon} alt="rv icon" />
                <p className="cart-option-title-text-active">Small</p>
                <p className="cart-option-price-text-active">$8.00</p>
              </div>
              <div className="cart-option-inactive">
                <img className="cart-otions-icon" src={rvIconInactive} alt="rv icon" />
                <p className="cart-option-title-text-inactive">Medium</p>
                <p className="cart-option-price-text-inactive">$9.00</p>
              </div>
              <div className="cart-option-inactive">
                <img className="cart-otions-icon" src={rvIconInactive} alt="rv icon" />
                <p className="cart-option-title-text-inactive">Large</p>
                <p className="cart-option-price-text-inactive">$12.00</p>
              </div>
            </div>
          </div>
          <div className="cart-details-container">
            <div className="cart-details-divider" />
            <div className="cart-details-row">
              <p className="cart-details-text">Lot:</p>
              <p className="cart-details-text">Spectrum South Lot</p>
            </div>
            <div className="cart-details-row">
              <p className="cart-details-text">Distance:</p>
              <p className="cart-details-text">5 minutes walking</p>
            </div>
            <div className="cart-details-row">
              <p className="cart-details-text">Open:</p>
              <p className="cart-details-text">6:00 PM</p>
            </div>
            <div className="cart-details-divider" />
            <div><iframe  className="cart-map-container" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q=Dee%20glem%20smith%20spectrum+(My%20Business%20Name)&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"></iframe></div>
            <div className="space-30" />
            <div className="cart-details-divider" />
            <div className="cart-details-row">
              <p className="cart-total-text">TOTAL</p>
              <p className="cart-total-text">$8.00</p>
            </div>
            <div className="cart-purchase-button-container">
              <div className="cart-purchase-button">
                <p classNames="cart-purchase-button-text">Purchase</p>
              </div>
            </div>
          </div>
        </div>
    </div>
  );
}
