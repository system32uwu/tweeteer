# Project Structure

```sh
tweeteer-
         |- backend: web server
		 |- frontend: web ui
		 |- docs: basic documentation
		 |- postman: postman requests
```

# backend

```sh
backend-
		|- api: modular routing of the API
		|- models: python classes equivalent to the database tables
		|- tools: utilities (script to create database, connect to database)
		|- config.py: flask config file
		|- server.py: flask web server
```

## backend/api
```sh
backend/api-
			|- v1: contains the first version of the api
			|- router.py: contains the main router for the api and error handlers.
```

### backend/api/v1
```sh
backend/api/v1-
			   |- auth.py: basic authentication functions (login, logout)
			   |- post.py: post CRUD
			   |- user.py: user CRUD
```

### backend/models
```sh
backend/models-
			   |- shared.py: contains the database connection
			   |- user.py: contains the user class, with CRUD functions
			   |- post.py: contains the post and comment classes, with CRUD functions
```