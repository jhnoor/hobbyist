# Hobbyist

## Requirements

* docker (>= 18.06)
* docker-compose (>= 1.22)
* node (>= 10)

## Setup

### Backend

In root
```
docker-compose up --build -d
```

This starts nginx, django and postgres docker containers. The django app requires certain commands to be run for the first run, you can either enter the container bash terminal:

```
docker exec -it django bash
python manage.py makemigrations
python manage.py migrate
```

OR run the command directly from your terminal:

```
docker exec -it django python manage.py makemigrations
docker exec -it django python manage.py migrate
```


### Frontend

In `src/react-client`
```
npm install
npm start
```

This starts the hot-reloading react server, with proxy to localhost:80


## API

URL | METHOD | EXPLANATION | Authentication
--- | --- | --- | ---
http://hobbyist.no/api/v2/projects/                 | GET   | Lists all the projects | ✅ Allow any
http://hobbyist.no/api/v2/projects/:id/             | GET   | Returns data for a single project by id | ✅ Allow any
http://hobbyist.no/api/v2/projects/:id/comment/     | POST  | Post a comment. Expected data: `{"text": "Here is my comment"}` | ⚠️ Post as anon
http://hobbyist.no/api/v2/projects/:id/upvote/      | PUT   | Upvote a project, increments the karma by one | ✅ Allow any
http://hobbyist.no/api/v2/projects/:id/downvote/    | PUT   | Downvote a project, decrements karma by one | ✅ Allow any
http://hobbyist.no/api/v2/auth/register/            | POST  | Register a user. Expected data: `{"username": "Tony_stark","password": "J4RV1S"}` | ✅ Allow any
http://hobbyist.no/api/v2/auth/login/               | POST  | Login a user. Expected data: `{"username": "Tony_stark","password": "J4RV1S"}` | ⛔️ Must be logged in
http://hobbyist.no/api/v2/auth/user/                | GET   | Get currently logged in user | ⛔️ Must be logged in





