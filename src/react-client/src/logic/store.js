import { createStore, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";
import { reducers } from "./reducers";

// Exportert funksjon som oppretter store, legg merke til at vi i tilleg bruker
// https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd
// dette vil vi ikke gjøre i produksjon, så det bør være logikk som ikke tar med denne med mindre
// man kjører i dev.
const enhancer = compose(
  applyMiddleware(thunk),
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);

export const store = createStore(reducers, enhancer);
