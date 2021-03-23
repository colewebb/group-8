import React, { useState, useEffect }  from "react";
import reactDom from "react-dom";
import Menu from '../../navigation/menu';
import "./lots.styles.css";
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import LotCard from './lotCard.js';
import Breadcrumbs from '../breadcrumbs/breadcrumbs';

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

  function FormRow() {
     return (
       <React.Fragment>
         <Grid item xs={12}>
           <LotCard />
         </Grid>

       </React.Fragment>
     );
   }

  return (
    <div className="events-view-root">
      <Menu />
      <Breadcrumbs />
      <h2 className="lots-list-title-text">Lots:</h2>
      <div className="lots-grid-view-root">
        <div className="lots-grid-view">
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
