from ariadne import MutationType
from datetime import datetime as dt
from models.rol import Rol
from models.rol_relation import RolRelation
from schemas.helpers.normalize import change_keys
from schemas.rol import RolCreate


mutations_resolvers = MutationType()


@mutations_resolvers.field("rolCreate")
async def resolve_rol_create(_, info, rol) -> dict:
    store_data = Rol.get_instance()
    data = RolCreate(**rol)
    normalize = change_keys(data.dict(exclude_none=True), key="_key")

    return await store_data.create(normalize)
