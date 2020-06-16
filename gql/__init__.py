from ariadne.executable_schema import make_executable_schema

from .schemas.enums import enums_defs
from .schemas.inputs import inputs_defs
from .schemas.mutations import mutations_defs
from .schemas.queries import queries_defs
from .schemas.scalars import scalars_defs
from .schemas.types import types_defs

from .resolvers.mutations import mutations_resolvers
from .resolvers.queries import queries_resolvers
from .resolvers.scalars import scalars_resolvers

schema_defs = f"{enums_defs}\n{inputs_defs}\n{mutations_defs}\n{queries_defs}\n{scalars_defs}\n{types_defs}"

schema = make_executable_schema(
    schema_defs, mutations_resolvers, queries_resolvers, scalars_resolvers
)
