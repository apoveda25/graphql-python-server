from fastapi import FastAPI
from ariadne.asgi import GraphQL
from gql import schema
from env.environment import Environment

env = Environment()
app = FastAPI()

app.mount("/graphql", GraphQL(schema, debug=True))
