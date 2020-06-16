import os
from ariadne.load_schema import load_schema_from_path

rol_query = load_schema_from_path(os.getcwd() + "/gql/schemas/queries/rol.graphql")
scope_query = load_schema_from_path(os.getcwd() + "/gql/schemas/queries/scope.graphql")
user_query = load_schema_from_path(os.getcwd() + "/gql/schemas/queries/user.graphql")

queries_defs = f"{rol_query}\n{scope_query}\n{user_query}"
