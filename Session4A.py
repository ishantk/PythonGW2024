# Conditional Operators
# ==, !=, >, <, >=, <=

cab_fare = 500
e_wallet = 500

result = e_wallet >= cab_fare

print("can i book the cab:", result)
print(type(result))

# Logical Operators -> and or

email = input("Enter Email: ")
password = input("Enter Password: ")

print("Is Login Success ??")
result = (email == "john@example.com") and (password == "john123")
print(result)

otp = 3027
user_otp = int(input("Enter OTP Received"))
print("Is OTP Correct??", otp == user_otp)


# Memebership Testing
# is, is not

a = 10
b = 10

print(a == b) # True
print(a is b) # True
print(a is not b) # False

# HW: Find Difference between == and is


speed = 60
time = 9

speed = speed * (5/18)
length = speed * time

print("Length of Train is:", length)

# HW: Find 5 Quantative Aptitude problems and solve them using operators

