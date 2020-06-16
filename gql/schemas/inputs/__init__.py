import os
from ariadne.load_schema import load_schema_from_path

rol_input = load_schema_from_path(os.getcwd() + "/gql/schemas/inputs/rol.graphql")
scope_input = load_schema_from_path(os.getcwd() + "/gql/schemas/inputs/scope.graphql")
user_input = load_schema_from_path(os.getcwd() + "/gql/schemas/inputs/user.graphql")

inputs_defs = f"{rol_input}\n{scope_input}\n{user_input}"
