import React from "react";
import "./breadcrumbs.css";
import Moment from 'moment';

export default function Breadcrumbs(props) {

  Moment.locale('en');
   var dt = props.date;

  return (
    <div class="breadcrumbs-view-root">
      <div class="breadcrumbs-sub-view">
       <h1 class="breadcrumbs-event-text">{props.name}</h1>
       <p class="breadcrumbs-location-text">{props.address}</p>
       <p class="breadcrumbs-time-text">{Moment(dt).format('MMMM Do YYYY, h:mm a')}</p>
      </div>
    </div>
  );
}
