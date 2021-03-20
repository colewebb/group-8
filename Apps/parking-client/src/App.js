import './App.css';
import React from 'react';
import Nav from './navigation/nav';
import Cart from './screens/cart/cart';
import Events from './screens/events/events';
import Login from './screens/login/login';
import Lots from './screens/lots/lots';
import Reservation from './screens/reservation/reservation';
import Reservations from './screens/reservations/reservations';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <Route path="/login" component={Login} />
        <Route path="/" exact component={Events} />
        <Route path="/events" component={Events} />
        <Route path="/lots" component={Lots} />
        <Route path="/cart" component={Cart} />
        <Route path="/reservation" component={Reservation} />
        <Route path="/reservations" component={Reservations} />
      </div>
    </Router>
  );
}

export default App;
