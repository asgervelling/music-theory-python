import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import "./App.css";
import Chord from "./components/Chord";
import Navbar from "./components/Navbar";

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Switch>
            <Route exact path="/">
              <Chord />
            </Route>
            <Route path="/other">
              <Chord />
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
