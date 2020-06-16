from ariadne import ObjectType
from datetime import datetime as dt
from models.rol import Rol

queries_resolvers = ObjectType("Query")
user = ObjectType("User")


@queries_resolvers.field("getRol")
async def get_rol(*_, key: str) -> dict:
    store_data = Rol.get_instance()

    return await store_data.find(key)


@user.field("has_rol")
async def has_rol(obj, info) -> dict:
    store_data = Rol.get_instance()

    return await store_data.find_edge_has_rol(obj["_id"])
