from models.base import BaseModel
from database.map_collections import map_collections


class Scope(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.name = map_collections["scope"]

    async def find(self, key: str) -> dict:
        bind_vars = {
            "@Scope": self.name,
            "_key": key,
        }

        query = """
            FOR scope IN @@Scope
            FILTER scope._key == @_key
            RETURN scope
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
                const { document, scope } = params

                const { _id } = db[scope].save(document);

                return db[scope].document(_id);
            }
        """

        return self.db.execute_transaction(
            command=command,
            params={"document": document, "scope": self.name,},
            read=[self.name],
            write=[self.name],
        )

    async def find_edge_has_scopes(self, id: str) -> [dict]:
        bind_vars = {
            "@RolRelation": map_collections["rol_relation"],
            "_id": id,
        }

        query = """
            FOR vertex, edge IN OUTBOUND @_id @@RolRelation
            FILTER edge.relation == 'has_scopes'
            RETURN vertex
        """

        cursor = self.db.aql.execute(query, bind_vars=bind_vars)

        return [doc for doc in cursor]
