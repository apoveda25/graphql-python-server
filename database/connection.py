import os
from arango import ArangoClient


class Connection:
    def __init__(self):
        self.ARANGODB_HOSTS = os.getenv("ARANGODB_HOSTS")
        self.ARANGODB_DATABASE = os.getenv("ARANGODB_DATABASE")
        self.ARANGODB_USER = os.getenv("ARANGODB_USER")
        self.ARANGODB_PASSWORD = os.getenv("ARANGODB_PASSWORD")

        self.client = ArangoClient(hosts=os.getenv("ARANGODB_HOSTS"))
        self.conn = self.client.db(
            self.ARANGODB_DATABASE,
            username=self.ARANGODB_USER,
            password=self.ARANGODB_PASSWORD,
        )
