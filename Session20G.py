"""
    MongoDB

    1. SignUp on MongoDb
    https://www.mongodb.com/cloud/atlas/register

    2. Create Cluster
        > Shared | Anyone of your choice (GCP/AWSAzure)
        > Region in India 
    
    3. Once, Cluster is created we need to configure access for it
        > Navigate to Network Access
        > Add IP Address as 0.0.0.0/0
          this meanas, we can access our MongoDB from any IP address

        > Navigate to Database Access
            Create a new user with password
        
        > Give your User, a Built In Role -> Admin Role

    4. In MongoDB Atlas, Create a new Project

    5. Navigate to DataBase > Browse Collections
        Now, create a new Database of your choice with a collection name

    6. Inside the Database > collection > insert a new Document
"""