import React from "react";
import "./steps.css";
import Moment from 'moment';

export default function Steps(props) {

  return (
    <div class="step-view-root">
      <div class="step-sub-view">
       <h1 class="step-title-text">Step {props.step}</h1>
       <div class="step-title-container-center">
         <div class="step-title-container">
           <p class={`step-text${props.step == 1 ? "-active" : ""}`}>Select Event</p>
           <p class={`step-text${props.step == 2 ? "-active" : ""}`}>Select Lot</p>
           <p class={`step-text${props.step == 3 ? "-active" : ""}`}>Checkout</p>
         </div>
       </div>
       <div class="step-bar-container">
         <div class="step-bar">
         {props.step == 1 ?
           <div class="step-bar-fill-10" />
         :
          <div />
         }
         {props.step == 2 ?
           <div class="step-bar-fill-50" />
         :
           <div />
         }
         {props.step == 3 ?
           <div class="step-bar-fill-100" />
         :
          <div />
         }
         </div>
       </div>
      </div>
    </div>
  );
}
