import './App.css';
import React from 'react';
import Menu from './navigation/menu';
import Cart from './screens/cart/cart';
import Events from './screens/events/events';
import Login from './screens/login/login';
import Account from './screens/account/account';
import Lots from './screens/lots/lots';
import Faq from './screens/faq/faq';
import Reservation from './screens/reservation/reservation';
import Reservations from './screens/reservations/reservations';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <Route path="/" exact component={Events} />
        <Route path="/login" component={Login} />
        <Route path="/events" component={Events} />
        <Route path="/account" component={Account} />
        <Route path="/lots" component={Lots} />
        <Route path="/cart" component={Cart} />
        <Route path="/reservation" component={Reservation} />
        <Route path="/reservations" component={Reservations} />
        <Route path="/faq" component={Faq} />
      </div>
    </Router>
  );
}

export default App;
