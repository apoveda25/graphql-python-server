import os
from ariadne.load_schema import load_schema_from_path

scope_action = load_schema_from_path(
    os.getcwd() + "/gql/schemas/enums/scope_action.graphql"
)

enums_defs = f"{scope_action}"
