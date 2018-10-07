import React, { Component } from "react";
import { connect } from "react-redux";
import "./project-metrics.css";
import { upvoteAction, downvoteAction } from "../../logic/action-creators";

class ProjectMetrics extends Component {
  constructor() {
    super();
    this.handleUpVote = this.handleUpVote.bind(this);
    this.handleDownVote = this.handleDownVote.bind(this);
  }

  handleUpVote() {
    const { id, upvoted } = this.props;
    !upvoted && this.props.upvote(id);
  }

  handleDownVote() {
    const { id, downvoted } = this.props;
    !downvoted && this.props.downvote(id);
  }

  render() {
    const { karma, noOfComments, upvoted, downvoted } = this.props;
    const karmaPrefix = karma >= 0 ? "+" : "";
    return (
      <div className="project-item--group metrics">
        <div className="karma">
          <button
            className={upvoted ? "up active" : "up"}
            onClick={this.handleUpVote}
          >
            <div className="arrow-up"></div>
          </button>
          <button
            className={downvoted ? "down active" : "down"}
            onClick={this.handleDownVote}
          >
            <div className="arrow-down"></div>
          </button>
        </div>
        <div className="karma-count">{`${karmaPrefix}${karma}`}</div>
        <div className="number-of-comments">{noOfComments}</div>
      </div>
    );
  }
}

const mapDispatchToProps = dispatch => {
  return {
    upvote: id => dispatch(upvoteAction(id)),
    downvote: id => dispatch(downvoteAction(id))
  };
};

const mapStateToProps = (state, props) => {
  const project = state.projects.find(project => project.id === props.id);
  return project ? project : {};
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ProjectMetrics);
