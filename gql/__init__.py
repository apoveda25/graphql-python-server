from ariadne.executable_schema import make_executable_schema

from gql.schemas.enums import enums_defs
from gql.schemas.inputs import inputs_defs
from gql.schemas.mutations import mutations_defs
from gql.schemas.queries import queries_defs
from gql.schemas.scalars import scalars_defs
from gql.schemas.types import types_defs

from .resolvers.mutations import mutations_resolvers
from .resolvers.queries import queries_resolvers
from .resolvers.scalars import scalars_resolvers

schema_defs = f"""
    {enums_defs}

    {inputs_defs}

    {mutations_defs}

    {queries_defs}

    {scalars_defs}

    {types_defs}
"""

schema = make_executable_schema(
    schema_defs, mutations_resolvers, queries_resolvers, scalars_resolvers
)
