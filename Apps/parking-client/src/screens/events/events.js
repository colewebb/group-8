import Breadcrumbs from '../breadcrumbs/breadcrumbs';
import React, { useState, useEffect }  from "react";
import reactDom from "react-dom";
import Menu from '../../navigation/menu';
import "./events.styles.css";
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import EventCard from './eventCard.js';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
}));
export default function Events(props) {
  const classes = useStyles();

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
    <div class="events-view-root">
      <Menu />
      <Breadcrumbs />
      <h2 class="events-title-text">Events</h2>
      <div class="grid-view-root">
        <div class="grid-view">
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
