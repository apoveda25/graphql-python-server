from models.base import BaseModel
from database.map_collections import map_collections


class RolRelation(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.name = map_collections["rol_relation"]

    async def create(self, document: dict) -> dict:
        command = """
            function (params) {
                const db = require('internal').db;
                const { document, rol_relation } = params

                const { _id } = db[rol_relation].save(document);

                return _id
            }
        """

        return self.db.execute_transaction(
            command=command,
            params={"document": document, "rol_relation": self.name,},
            read=[self.name],
            write=[self.name],
        )
