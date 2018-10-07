import React, { Component } from "react";
import { BrowserRouter as Router, Redirect, Route } from "react-router-dom";

import Navbar from "./navbar";
import ProjectsList from "./projects-list";
import Project from "./project";
import "./app.css";

export default class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Navbar />

          <Route path="/projects-list" component={ProjectsList} />
          <Route
            path="/project/:id"
            render={props => <Project key={props.match.params.id} {...props} />}
          />
          <Route
            exact
            path="/"
            component={() => <Redirect to="/projects-list" />}
          />
        </div>
      </Router>
    );
  }
}
