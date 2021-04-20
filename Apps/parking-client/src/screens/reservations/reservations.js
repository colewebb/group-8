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
    fetch(`http://localhost:8000/api/users/${localStorage.getItem('id')}/reservations/`, {
            headers: {
              Authorization: `JWT ${localStorage.getItem('token')}`
            }
          })
      .then(res => res.json())
      .then(
        (result) => {
          console.log(result);
          setIsLoaded(true);
          if(result[0]){
            setItems(result);
          }else{
            setItems([result]);
          }
        },
        (error) => {
          // localStorage.setItem('token', '');
          // localStorage.setItem('username', '');
          // localStorage.setItem('id', '');
          // window.location = "/";
        }
      )
  }, [])


  function FormRow(props) {
     return (
       <React.Fragment>
         <Grid item xs={12}>
           <ReservationCard id={props.id} eventId={props.eventId}/>
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
              <FormRow id={item.id} eventId={item.event}/>
            </Grid>
          ))}
         </Grid>
       </div>
     </div>
    </div>
  );
}
