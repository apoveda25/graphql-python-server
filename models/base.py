from arango import ArangoClient

from database.connection import Connection


class BaseModel:
    _instance = None
    name = ""

    @classmethod
    def get_instance(cls):  # Constructor alternativo que retorna una nueva instancia
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        # self.name = self.__class__.name
        connection = Connection()
        self.db = connection.conn
        # self.collection = self.db.collection(self.name)
        self.aql = self.db.aql

    # async def get(self, key):
    #     document = self.collection.get(key)

    #     if document == None:
    #         return False

    #     return document

    # async def get_many(self, _list):
    #     document = self.collection.get_many(_list)

    #     if document == None:
    #         return False

    #     return document

    async def save(self, document: dict):
        command = """
            function (params) {
                const db = require('internal').db;
                const { collection, document } = params

                const { _id, _key } = db[collection].save(document);

                return { _id, _key };
            }
        """

        return self.db.execute_transaction(
            command=command,
            params={"document": document, "collection": self.name},
            read=[self.name],
            write=[self.name],
        )

    async def update(self, document: dict):
        command = """
            function (params) {
                const db = require('internal').db;
                const { collection, document } = params;
                const collect = db[collection];

                const { _id, _key } = collect.update(document, document);

                return { _id, _key };
            }
        """

        return self.db.execute_transaction(
            command=command,
            params={"document": document, "collection": self.name},
            read=[self.name],
            write=[self.name],
        )

    async def update_many(self, documents: list):
        command = """
            function (params) {
                const db = require('internal').db;
                const { collection, documents } = params;

                const result = documents.map(document => {
                    const { _id, _key } = db[collection].update(document._key, document);

                    return { _id, _key };
                });

                return result;
            }
        """

        return self.db.execute_transaction(
            command=command,
            params={"documents": documents, "collection": self.name},
            read=[self.name],
            write=[self.name],
        )

    # async def count(self):
    #     query = """
    #         RETURN LENGTH(@@Collection)
    #     """

    #     bind_vars = {"@Collection": self.name}

    #     cursor = self.db.aql.execute(query, bind_vars=bind_vars)

    #     return [count for count in cursor]
