import mysql.connector as db
from Session13 import Customer

# # Database username and password
# username = "root"
# password = ""

# # Localhost
# host = "127.0.0.1"
# database = "gw2024pds"

# 1: Create Connection
connection = db.connect(user="root", 
                        password="", 
                        host="127.0.0.1", 
                        database="gw2024pds",
                        )

print("Connection Created.")
print(connection)

customer = Customer()
customer.add_customer_details()

# 2: Create SQL Statement
# sql = "insert into Customer values(null, 'John', '+91 99999 11111', 'john@example,com', 20, 'male')"
sql = "insert into Customer values(null, '{}', '{}', '{}', {}, '{}')".format(customer.name, customer.phone, customer.email, customer.age, customer.gender)

# 3: Obtain Cursor -> Perfom CRUD Operations with MySQL
cursor = connection.cursor()

# 4: Execute SQL Command
cursor.execute(sql)

# 5: Commit the Write Operation
connection.commit()

print("SQL Statement Executed...")

