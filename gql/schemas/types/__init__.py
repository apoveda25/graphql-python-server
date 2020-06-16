import os
from ariadne.load_schema import load_schema_from_path

rol = load_schema_from_path(os.getcwd() + "/gql/schemas/types/rol.graphql")
scope = load_schema_from_path(os.getcwd() + "/gql/schemas/types/scope.graphql")
user = load_schema_from_path(os.getcwd() + "/gql/schemas/types/user.graphql")

types_defs = f"{rol}\n{scope}\n{user}"
