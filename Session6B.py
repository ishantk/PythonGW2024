def square(num):
    print("1. num is:", num, id(num)) # 10
    num = num * num # 100
    print("2. num is:", num, id(num)) # 100
    # return

# Functions exists in memory
# print("square:", square) # hashcode and name of function

number = 10
print("A. number is:", number, id(number)) # 10
square(number)
print("B. number is:", number, id(number)) # 10
