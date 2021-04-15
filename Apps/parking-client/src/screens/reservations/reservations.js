import Breadcrumbs from '../breadcrumbs/breadcrumbs';
import React, { useState, useEffect } from 'react'
import reactDom from "react-dom";
import Menu from '../../navigation/menu';
import "./reservations.styles.css";
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import ReservationCard from './reservationCard.js';

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
export default function Reservations(props) {
  const classes = useStyles();
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);
  const [events, setEvents] = useState([]);


  useEffect(() => {
    fetch("http://localhost:8000/api/reservations/", {
            headers: {
              Authorization: `JWT ${localStorage.getItem('token')}`
            }
          })
      .then(res => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setItems(result);
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
    fetch("http://localhost:8000/api/events/5/")
      .then(res => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setEvents(result);
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          setIsLoaded(true);
          setError(error);
          window.location = "/";
        }
      )
  }, [])


  function FormRow(props) {
     return (
       <React.Fragment>
         <Grid item xs={12}>
           <ReservationCard id={props.id} name={props.name} startTime={props.startTime} address={props.address}/>
         </Grid>

       </React.Fragment>
     );
   }

  return (
    <div class="events-view-root">
      <Menu />
      <h2 class="events-title-text">My Reservations</h2>
      <div class="grid-view-root">
        <div class="grid-view">
          <Grid container spacing={1}>
          {items.map(item => (
            <Grid key={item.id} container item xs={12} spacing={0}>
              <FormRow id={item.id} name={events.name} startTime={events.startTime} address={events.address}/>
            </Grid>
          ))}
         </Grid>
       </div>
     </div>
    </div>
  );
}
