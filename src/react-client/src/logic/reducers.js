import {
  UP_VOTE,
  DOWN_VOTE,
  GET_PROJECTS_BEGIN,
  GET_PROJECTS_SUCCESS,
  GET_PROJECTS_FAILURE
} from "./action-types";

// Reducer
// en funksjon som tar state (defaulter til 0) og en action
// basert på action.type, øker eller reduserer state-variablene count med 1

const initialState = {
  projects: []
};

export const reducers = (state = initialState, action) => {
  switch (action.type) {
    case UP_VOTE:
      return Object.assign({}, state, {
        projects: state.projects.map(project => {
          return project.id === action.id
            ? Object.assign({}, project, {
                karma: project.karma + 1,
                upvoted: true,
                downvoted: false
              })
            : project;
        })
      });

    case DOWN_VOTE:
      return Object.assign({}, state, {
        projects: state.projects.map(project => {
          return project.id === action.id
            ? Object.assign({}, project, {
                karma: project.karma - 1,
                upvoted: false,
                downvoted: true
              })
            : project;
        })
      });

    // GET PROJECTS ACTIONS
    case GET_PROJECTS_BEGIN:
      return {
        ...state,
        loading: true,
        error: null
      };
    case GET_PROJECTS_SUCCESS:
      return {
        ...state,
        loading: false,
        projects: action.payload.projects
      };
    case GET_PROJECTS_FAILURE:
      return {
        ...state,
        loading: false,
        error: action.payload.error,
        projects: []
      };
    default:
      return state;
  }
};
