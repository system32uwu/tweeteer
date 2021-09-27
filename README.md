# Tweeteer - an innovative social network

Tweeteer aims to become the #1 social network through a vast set of modern features, such as:

- creating an account
- posting
- commenting posts
- liking posts

## Project Structure

```sh
 |- backend: web server
 |- frontend: web ui
 |- docs: basic documentation
 |- postman: postman requests
```

### backend

```sh
 |- api: modular routing of the API
 |- models: python classes equivalent to the database tables
 |- tools: utilities (script to create database, connect to database)
 |- config.py: flask config file
 |- server.py: flask web server
```

#### backend/api

```sh
 |- v1: contains the first version of the api
 |- router.py: contains the main router for the api and error handlers.
```

#### backend/api/v1

```sh
 |- auth.py: basic authentication functions (login, logout)
 |- post.py: post CRUD
 |- user.py: user CRUD
```

#### backend/models

```sh
 |- shared.py: contains the database connection
 |- user.py: contains the user class, with CRUD functions
 |- post.py: contains the post and comment classes, with CRUD functions
```

[Walkthrough](https://docs.google.com/presentation/d/1AeGjL2gGYHjohZK8petAJ87p2tiBSyt2Qem_fufOvAM/edit?usp=sharing)
