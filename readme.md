# Touch my coding Backend-server

## Environment Setting

- You should set virtual environment Python 3.8
- Recommend to use virtualenv
- You can download python package from

```
pip install -r requirements.txt
```

## Create virtual environment

```
# Create virtual env
virtualenv env --python=python3.8
```

## Set SqlAlchemy

This project use Flask Sql Alchemy as ORM libraries.

Need environment file ".env"

```
.env

DB_USER=
DB_PW=
DB_HOST=
DB_PORT=
DB_DATABASE=
```

Reference below commands

```
# First init
flask db init

# Create migration
flask db migrate

# Migration update
flask db upgrade
```

ref: https://blogger.pe.kr/887

## Vision Api

In this project, Vision Api was used. So, it needs API key value for request server.

```
.env
~~
API_KEY=

```
