from ariadne import MutationType
from datetime import datetime as dt
from models.user import User
from schemas.helpers.normalize import change_keys
from schemas.user import UserCreate


mutations_resolvers = MutationType()


@mutations_resolvers.field("userCreate")
async def resolve_user_create(parent, info, user) -> dict:
    store_data = User.get_instance()
    data = UserCreate(**user)
    normalize = change_keys(data.dict(exclude_none=True), key="_key")

    return await store_data.create(normalize)
