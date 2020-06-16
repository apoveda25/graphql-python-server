from ariadne import MutationType
from datetime import datetime as dt
from models.scope import Scope
from schemas.helpers.normalize import change_keys
from schemas.scope import ScopeCreate


mutations_resolvers = MutationType()


@mutations_resolvers.field("scopeCreate")
async def resolve_scope_create(_, info, scope) -> dict:
    store_data = Scope.get_instance()
    data = ScopeCreate(**scope, key=f'{scope["collection"]}{scope["action"]}')
    normalize = change_keys(data.dict(exclude_none=True), key="_key")

    return await store_data.create(normalize)
