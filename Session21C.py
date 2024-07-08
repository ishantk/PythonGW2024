from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

class MongoDBHelper:

    def __init__(self, collection="users"):
        uri = "mongodb+srv://atpl:atpl@cluster0.eh8zx.gcp.mongodb.net/?appName=Cluster0"

        # Only if you face SSL error
        ca = certifi.where()

        # Create a new client and connect to the server
        # client = MongoClient(uri, server_api=ServerApi('1'))

        # Only if you face SSL error, add -> tlsCAFile=ca
        client = MongoClient(uri, tlsCAFile=ca, server_api=ServerApi('1'))  

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        # Get reference to the database
        self.db = client['gw2024pds']
        self.collection = self.db[collection]

    def insert(self, document):
        self.collection.insert_one(document)
        print("Document inserted in Collection:", self.collection.name)

    def fetch(self, query=""):
        documents = self.collection.find(query)
        return list(documents)