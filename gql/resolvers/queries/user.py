from ariadne import ObjectType
from datetime import datetime as dt
from models.user import User

queries_resolvers = ObjectType("Query")


@queries_resolvers.field("getUser")
async def get_user(parent, info, key: str) -> dict:
    store_data = User.get_instance()

    return await store_data.find(key)
