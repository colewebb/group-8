import Breadcrumbs from '../breadcrumbs/breadcrumbs';
import Steps from '../steps/steps';
import React, { useState, useEffect } from 'react'
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
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/events/", {
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`
        }
      })
      .then(res => res.json())
      .then(
        (result) => {

          if(result[0]){
            setIsLoaded(true);
            setItems(result);
          }else{
            localStorage.setItem('token', '');
            localStorage.setItem('username', '');
            localStorage.setItem('id', '');
            window.location = "/loggedout";
          }
        },
        (error) => {
          localStorage.setItem('token', '');
          localStorage.setItem('username', '');
          localStorage.setItem('id', '');
          window.location = "/loggedout";
        }
      )
  }, [])


  function FormRow(props) {
     return (
       <React.Fragment>
         <Grid item xs={12}>
           <EventCard id={props.id} name={props.name} startTime={props.startTime} address={props.address}/>
         </Grid>

       </React.Fragment>
     );
   }

  return (
    <div class="events-view-root">
      <Menu />
      <Steps step={1}/>
      <h2 class="events-title-text">Utah State Events</h2>
      <div class="grid-view-root">
        <div class="grid-view">
          <Grid container spacing={1}>
          {items.map(item => (
            <Grid key={item.id} container item xs={12} spacing={0}>
              <FormRow id={item.id} name={item.name} startTime={item.startTime} address={item.address}/>
            </Grid>
          ))}
         </Grid>
       </div>
     </div>
    </div>
  );
}
