def add(num1, num2):
    result = num1 + num2
    print("result is: {}".format(result))

print(hex(id(add)))
print("add is:", add) # add is a function and you will the hashcode of function

# Execute the add function
add(10, 20)

# Reference Copy Operation
hello = add

hello(11, 22)

# If you redefine the same function, the previous function will be removed from memory
# And new defintion will exist
def add(num1, num2, num3):
    result = num1 + num2 + num3 + 10
    print("result is:", result)

print(hex(id(add)))
print("add is:", add)

add(10, 20, 30)