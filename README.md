# VANNA.AI DEMO

A demo of [Vanna.AI](https://vanna.ai/) using OpenAI LLM, Chroma DB and PostgreSQL

## Prerequisites

1. You have Docker, Python and [Poetry](https://github.com/python-poetry/poetry) installed.
2. You have an an OpenAI API key.

## Getting started

Install dependencies

```
poetry install
```

Rename `.env.example` to `.env` and add your OpenAI API key.

Run docker compose:

```
docker-compose up
```

The docker compose file should start the Postgres server, create a database called `dvdrental` and load data into it (see `init.sh` file).

More information regarding the `dvdrental` database can be found [here](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/).

Start the UI app:

```
poetry run python main.py
```

Open [http://localhost:8084](http://localhost:8084)
