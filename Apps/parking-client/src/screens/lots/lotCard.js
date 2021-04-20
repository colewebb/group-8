import React from "react";
import reactDom from "react-dom";
import "./lotCard.css";
import Menu from '../../navigation/menu';

export default function lotCard(props) {
  return (
    <div className="lot-card-root">
      <div className="lot-card-container">
        <div className="lot-card-price-container">
          <p className="lot-card-price-text">$10.00</p>
        </div>
        <div className="lot-card-info-container">
            <p className="lot-card-name-text">South Spectrum Lot</p>
            <div className="lot-card-info-row">
              <div>
                <p className="lot-card-info-text">6:30pm</p>
                <p className="lot-card-info-sub-text">Open Time</p>
              </div>
              <div>
                <p className="lot-card-info-text">0.03 miles</p>
                <p className="lot-card-info-sub-text">Distance</p>
              </div>
              <div>
                <p className="lot-card-info-text">150</p>
                <p className="lot-card-info-sub-text">spots</p>
              </div>
            </div>
        </div>
      </div>
    </div>
  );
}
