import os
from ariadne.load_schema import load_schema_from_path

rol_mutation = load_schema_from_path(os.getcwd() + "/gql/schemas/mutations/rol.graphql")
scope_mutation = load_schema_from_path(
    os.getcwd() + "/gql/schemas/mutations/scope.graphql"
)
user_mutation = load_schema_from_path(
    os.getcwd() + "/gql/schemas/mutations/user.graphql"
)

mutations_defs = f"{rol_mutation}\n{scope_mutation}\n{user_mutation}"
