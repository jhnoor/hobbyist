import React, { Component } from "react";
import { Link } from "react-router-dom";
import "./project-item.css";
import ProjectMetrics from "../project-metrics";

export default class ProjectItem extends Component {
  static defaultProps = {
    description: "no description",
    comments: []
  };

  render() {
    const { id, karma, comments, title, description } = this.props;
    return (
      <div className="project-item">
        <ProjectMetrics id={id} karma={karma} noOfComments={comments.length} />
        <div className="project-item--group">
          <Link to={`project/${id}`} className="project-item--title">
            {title}
          </Link>
          <div className="project-item--description">{description}</div>
        </div>
      </div>
    );
  }
}
