import './App.css';
import React from 'react';
import Cart from './screens/cart/cart';
import Events from './screens/events/events';
import Login from './screens/login/login';
import Register from './screens/register/register';
import Account from './screens/account/account';
import Lots from './screens/lots/lots';
import Faq from './screens/faq/faq';
import Fourofour from './screens/fourofour/fourofour';
import Loggedout from './screens/loggedout/loggedout';
import Reservation from './screens/reservation/reservation';
import Reservations from './screens/reservations/reservations';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Map from './screens/map/map';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route exact path="/" component={Events} />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route exact path="/events" component={Events} />
          <Route path="/account" component={Account} />
          <Route path="/events/*/lots" exact component={Lots} />
          <Route path="/events/*/lots/cart/*" component={Cart} />
          <Route path="/reservation" component={Reservation} />
          <Route path="/reservations" component={Reservations} />
          <Route path="/faq" component={Faq} />
          <Route path="/map" component={Map} />
          <Route path="/loggedout" component={Loggedout} />
          <Route path="*" component={Fourofour} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
