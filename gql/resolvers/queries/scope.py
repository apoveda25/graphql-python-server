from ariadne import ObjectType
from datetime import datetime as dt
from models.scope import Scope

queries_resolvers = ObjectType("Query")
rol = ObjectType("Rol")


@queries_resolvers.field("getScope")
async def get_scope(*_, key: str) -> dict:
    store_data = Scope.get_instance()

    return await store_data.find(key)


@rol.field("has_scopes")
async def has_scope(obj, info) -> dict:
    store_data = Scope.get_instance()

    return await store_data.find_edge_has_scopes(obj["_id"])
