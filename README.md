## Description

This is a simple API that gets the name of a city, and returns a playlist according to the current temperature of this city.

This API is implemented in production on an EC2 and its database on an RDS on the AWS.

You can access it through the link: http://52.67.150.239:17010/docs

NOTE: The instance is without ssl certificate because I am using the free version.

## Projects Resources

- Languege: Python 3.6
- Package manager: pip
- Main dependencies: [_Flask 1.0.2_](https://flask.palletsprojects.com/en/1.1.x/), [_Flask-Restplus 0.13.0_](https://flask-restplus.readthedocs.io/en/stable/), [_SQLAlchemy 1.3.8_](https://docs.sqlalchemy.org/en/13/orm/tutorial.html), [_Alembic 1.2.1_](https://alembic.sqlalchemy.org/en/latest/tutorial.html), [_Tekore_](https://tekore.readthedocs.io/en/stable/)
- DB: [_MySQL 5.7_](https://dev.mysql.com/doc/refman/5.7/en/)

## Installation

First of all, clone this project in your work environment.

`$ git clone https://github.com/ymussi/maju-playlist.git`

and after that choice your runing method:

## Running local

```bash
$ pip install -r requirements.txt
$ python setup.py develop
$ cd maju/
$ python run.py
```

The API Doc can be accessed at: http://localhost:5000/docs

## Running with docker container

Using the docker compose, the web services and database, will be configured and started automatically in the container through the following command line:

`$ docker-compose up`

The API Doc can be accessed at: http://localhost:8000/docs

## Database Server

The database server will be exposed externally on:

- host: localhost
- username: maju
- password: maju
- port: 23307
- database: maju_playlist


## Runing migrations

```bash
$ cd maju/
$ alembic upgrade head
```

## Working

To get a playlist

- Send a GET request to endpoint: **/playlist/<city_name>**

To get a statistics:

- Send a GET request to endpoint: **/statistics**

PS: My access key to the weatherpi only allows me to consult 10 cities and make 400 requests per day because it is a free account.

## Logs

- the logs can be seen by the metabase on: http://52.67.150.239:17030/public/dashboard/a54ddf1c-6ad2-42ae-bd88-28e7642301bc

## Testes

- As this api does not perform mutations, no tests have been implemented.


Copyright (c) [2020] [Yuri Mussi]
