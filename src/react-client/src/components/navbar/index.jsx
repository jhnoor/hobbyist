import React, { PureComponent } from "react";
import { NavLink } from "react-router-dom";
import "./navbar.css";

export default class Navbar extends PureComponent {
  render() {
    return (
      <div>
        <div className="top-header">
          <a className="logo" href="/">
            Hobbyist
          </a>
        </div>
        <nav className="links-header">
          <NavLink to="/projects-list" className="link">
            Projects
          </NavLink>
        </nav>
      </div>
    );
  }
}
