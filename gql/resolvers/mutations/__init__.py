from .rol import mutations_resolvers as rol_resolvers
from .scope import mutations_resolvers as scope_resolvers
from .user import mutations_resolvers as user_resolvers

mutations_resolvers = [
    rol_resolvers,
    scope_resolvers,
    user_resolvers,
]
