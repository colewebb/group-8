import Breadcrumbs from '../breadcrumbs/breadcrumbs';
import React, { useState, useEffect }  from "react";
import reactDom from "react-dom";
import Menu from '../../navigation/menu';
import "./events.styles.css";
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import EventCard from './eventCard.js';



export default function Events(props) {

  function FormRow() {
     return (
       <React.Fragment>
         <Grid item xs={12}>
           <EventCard />
         </Grid>
       </React.Fragment>
     );
   }

  return (
    <div className="events-view-root">
      <Menu />
      <h2 className="events-title-text">Events</h2>
      <div className="grid-view-root">
        <div className="grid-view">
          <Grid container spacing={1}>
           <Grid container item xs={12} spacing={0}>
             <FormRow />
           </Grid>
           <Grid container item xs={12} spacing={0}>
             <FormRow />
           </Grid>
           <Grid container item xs={12} spacing={0}>
             <FormRow />
           </Grid>
           <Grid container item xs={12} spacing={0}>
             <FormRow />
           </Grid>
         </Grid>
       </div>
     </div>
    </div>
  );
}
