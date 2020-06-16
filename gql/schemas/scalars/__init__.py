import os
from ariadne.load_schema import load_schema_from_path

scalars = load_schema_from_path(os.getcwd() + "/gql/schemas/scalars/schema.graphql")

scalars_defs = f"{scalars}"
