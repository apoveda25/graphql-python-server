from models.base import BaseModel
from database.map_collections import map_collections


class Rol(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.name = map_collections["rol"]

    async def find(self, key: str) -> dict:
        bind_vars = {
            "@Rol": self.name,
            "_key": key,
        }

        query = """
            FOR rol IN @@Rol
            FILTER rol._key == @_key
            RETURN rol
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
                const { document, rol } = params

                const { _id } = db[rol].save(document);

                return db[rol].document(_id);
            }
        """

        return self.db.execute_transaction(
            command=command,
            params={"document": document, "rol": self.name,},
            read=[self.name],
            write=[self.name],
        )

    async def find_edge_has_rol(self, id: str) -> dict:
        bind_vars = {
            "@CompanyRelation": map_collections["company_relation"],
            "@UserRelation": map_collections["user_relation"],
            "_id": id,
        }

        query = """
            FOR vertex, edge IN OUTBOUND @_id @@CompanyRelation, @@UserRelation
            FILTER edge.relation == 'has_rol'
            RETURN vertex
        """

        cursor = self.db.aql.execute(query, bind_vars=bind_vars)

        docs = [doc for doc in cursor]

        if len(docs) == 0:
            return {}

        return docs[0]
