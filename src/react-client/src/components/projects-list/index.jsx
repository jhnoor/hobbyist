import React, { Component } from "react";
import ProjectItem from "../project-item";
import { connect } from "react-redux";

import { getProjectsAction } from "../../logic/action-creators";

class ProjectsList extends Component {
  componentDidMount() {
    this.props.dispatch(getProjectsAction());
  }

  render() {
    const { error, loading, projects } = this.props;
    if (error) {
      return <div>Error: {error.message}</div>;
    }

    if (loading) {
      return <div>Loading...</div>;
    }

    return (
      <div>
        <h3 className="page-title">All projects</h3>
        <div className="page-container">
          <div className="list">
            {projects.map(project => (
              <ProjectItem
                key={project.id}
                id={project.id}
                title={project.title}
                description={project.description}
                karma={project.karma}
                comments={project.comments}
              />
            ))}
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  projects: state.projects,
  loading: state.loading,
  error: state.error
});

export default connect(mapStateToProps)(ProjectsList);
