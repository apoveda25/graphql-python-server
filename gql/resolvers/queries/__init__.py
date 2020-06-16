from .rol import queries_resolvers as rol_resolvers
from .scope import queries_resolvers as scope_resolvers
from .user import queries_resolvers as user_resolvers

from .rol import user as user_has_rol

from .scope import rol as has_scope

queries_resolvers = [
    rol_resolvers,
    scope_resolvers,
    user_resolvers,
    user_has_rol,
    has_scope,
]
