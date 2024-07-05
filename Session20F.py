# String Formatting
name = "Leo"
age = "20"
email = "leo@example.com"

contact={
    "name": "Leo",
    "age":"20",
    "email":"leo@example.com"
}

print("name:", name, "age:", age, "email:", email)

print("name: {}, age: {}, email: {}".format(name, age, email))
print("name: {0}, age: {1}, email: {2}".format(name, age, email))
print("name: {2}, age: {1}, email: {0}".format(name, age, email))
print("name: {na}, age: {ag}, email: {em}".format(na=name, ag=age, em=email))

print("name: {name}, age: {age}, email: {email}".format_map(contact))