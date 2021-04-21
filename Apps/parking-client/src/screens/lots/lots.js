import Breadcrumbs from '../breadcrumbs/breadcrumbs';
import Steps from '../steps/steps';
import React, { useState, useEffect } from 'react'
import reactDom from "react-dom";
import Menu from '../../navigation/menu';
import "./lots.styles.css";
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import LotCard from './lotCard.js';

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
export default function Lots(props) {
  const classes = useStyles();
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);
  const [events, setEvents] = useState([]);

  const currentUrl = window.location.href;

  function getLotId(url){
    let re = /(?<=events\/)(.*)(?=\/lots)/i;
    return re.exec(url)[0];
  }

  useEffect(() => {
    fetch(`http://localhost:8000/api/events/${getLotId(currentUrl)}/lots/`, {
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
        (error) => {
          localStorage.setItem('token', '');
          localStorage.setItem('username', '');
          localStorage.setItem('id', '');
          window.location = "/loggedout";
          setError(error);
        }
      )
      fetch(`http://localhost:8000/api/events/${getLotId(currentUrl)}/`, {
              headers: {
                Authorization: `JWT ${localStorage.getItem('token')}`
              }
            })
        .then(res => res.json())
        .then(
          (result) => {
            setIsLoaded(true);
            setEvents(result);
          },
          (error) => {
            window.location = "/loggedout";
            setError(error);
          }
        )
  }, [])


  function FormRow(props) {
     return (
       <React.Fragment>
         <Grid item xs={12}>
           <LotCard id={props.id} capMediumActual={props.capMediumActual} capMediumMax={props.capMediumMax} capLargeActual={props.capLargeActual} capLargeMax={props.capLargeMax} capSmallActual={props.capSmallActual} capSmallMax={props.capSmallMax} name={props.name} openTime={props.openTime} address={props.address} costSmall={props.costSmall} costMedium={props.costMedium} costLarge={props.costLarge}/>
         </Grid>

       </React.Fragment>
     );
   }

  return (
    <div class="events-view-root">
      <Menu />
      <Steps step={2}/>
      <Breadcrumbs name={events.name} address={events.address} date={events.startTime}/>
      <h2 class="lot-title-text">Parking Options:</h2>
      <div class="grid-view-root">
        <div class="grid-view">
          <Grid container spacing={1}>
          {items.map(item => (
            <Grid key={item.id} container item xs={12} spacing={0}>
              <FormRow id={item.id} capMediumActual={item.capMediumActual} capMediumMax={item.capMediumMax} capLargeActual={item.capLargeActual} capLargeMax={item.capLargeMax} capSmallActual={item.capSmallActual} capSmallMax={item.capSmallMax} name={item.name} openTime={item.openTime} address={item.address} costSmall={item.costSmall} costMedium={item.costMedium} costLarge={item.costLarge}/>
            </Grid>
          ))}
         </Grid>
       </div>
     </div>
    </div>
  );
}
