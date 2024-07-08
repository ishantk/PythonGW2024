"""
    MongoDB CRUD Operations
    1. Install the Pymonog Library
        pip install "pymongo[srv]"
    2. Iff you face any error for SSL
        pip install certifi     
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

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
db = client['gw2024pds']

# Get Collection Names from DataBase
collections = db.list_collection_names()

for collection in collections:
    print(collection)


documents = db['users'].find()
print(documents)

for document in documents:
    print(document)
