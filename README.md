# Graphql Python Server

[Graphql](https://graphql.org/) server written in Python, uses [FastAPI](https://fastapi.tiangolo.com/) asynchronous framework, graphql [Ariadne](https://ariadnegraphql.org/) engine and [ArangoDB](https://www.arangodb.com/) database.
A high performance working stack with clean and easy python syntax.
Use it however you want, although it's just a starting point.

### Requirements

1. Install poetry `pip install poetry`

### Starting

1. Clone the repository `git clone https://github.com/apoveda25/graphql-python-server.git`

2. Enter the repository folder `cd graphql-python-server/`

3. Create a virtual environment `poetry shell`

4. Open with vscode `code .`

5. Install dependencies `poetry install`

6. Start server `uvicorn main:app --reload --port 8000`

7. Enter the url `http://localhost:8000/graphql/`
