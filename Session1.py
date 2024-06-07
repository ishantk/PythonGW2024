# Our Very First Program
# Containers

# Single Value Container

# Create Statement -> You are creating a SVC in RAM

# user_name is a REFERENCE VARIABLE
user_name = "auribises"

# Read Statement -> To read data inside a container
print(user_name, id(user_name), type(user_name))

# UPDATE Statement
user_name = 1001

print(user_name, id(user_name), type(user_name))

# DELETE Statement
del user_name

print(user_name, id(user_name), type(user_name))