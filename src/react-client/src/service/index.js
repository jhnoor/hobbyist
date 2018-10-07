import axios from "axios";

const URL_BASE = "/api/v2/";
const URL_PROJECTS = "projects/";
const URL_DOWNVOTE = "upvote/";
const URL_UPVOTE = "downvote/";

const handleError = error => {
  console.error(error); // TODO modal for this?
};

const getRequest = ({ url, params = {} }) => {
  const method = "get";

  return new Promise(resolve => {
    axios({
      method,
      baseURL: URL_BASE,
      url,
      params
    })
      .then(response => {
        resolve(response);
      })
      .catch(error => {
        throw new Error(`
        ${method} request failed with url: ${URL_BASE}${url}
        and params: ${JSON.stringify(params)},
        original error: ${JSON.stringify(error)}
        `);
      });
  });
};

const putRequest = ({ url }) => {
  const method = "put";
  return new Promise(resolve => {
    axios({
      method,
      baseURL: URL_BASE,
      url
    })
      .then(response => {
        resolve(response);
      })
      .catch(error => {
        throw new Error(`
        ${method} request failed with url: ${url}
        original error: ${JSON.stringify(error)}
         `);
      });
  });
};

export const getProjects = ({ id = "" }) => {
  const url = `${URL_PROJECTS}${id}/`;
  return new Promise(resolve => {
    try {
      getRequest({ url }).then(response => {
        resolve(response);
      });
    } catch (error) {
      handleError(error);
    }
  });
};

export const putProjectDownvote = ({ id }) => {
  const url = `${URL_PROJECTS}${id}/${URL_DOWNVOTE}`;
  return new Promise(resolve => {
    try {
      putRequest({ url }).then(response => {
        resolve(response);
      });
    } catch (error) {
      handleError(error);
    }
  });
};

export const putProjectUpvote = ({ id }) => {
  const url = `${URL_PROJECTS}${id}/${URL_UPVOTE}`;
  return new Promise(resolve => {
    try {
      putRequest({ url }).then(response => {
        resolve(response);
      });
    } catch (error) {
      handleError(error);
    }
  });
};
