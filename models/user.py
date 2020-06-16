from models.base import BaseModel
from database.map_collections import map_collections


class User(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.name = map_collections["user"]

    async def find(self, key: str) -> dict:
        bind_vars = {
            "@User": self.name,
            "_key": key,
        }

        query = """
            FOR user IN @@User
            FILTER user._key == @_key
            RETURN user
        """

        cursor = self.db.aql.execute(query, bind_vars=bind_vars)

        docs = [doc for doc in cursor]

        if len(docs) == 0:
            return {}

        return docs[0]

    async def create(self, document: dict) -> dict:
        command = """
            function (params) {
                const db = require('internal').db;
                const { user, document, rol, user_relation, rol_id, relation } = params

                db[rol].document(rol_id)

                const { _id } = db[user].save(document);
                db[user_relation].save({_from: _id, _to: rol_id, relation});

                return db[user].document(_id);
            }
        """

        return self.db.execute_transaction(
            command=command,
            params={
                "document": document,
                "user": self.name,
                "rol": map_collections["rol"],
                "user_relation": map_collections["user_relation"],
                "rol_id": f'{map_collections["rol"]}/client',
                "relation": "has_rol",
            },
            read=[self.name, map_collections["rol"], map_collections["user_relation"]],
            write=[self.name, map_collections["rol"], map_collections["user_relation"]],
        )
