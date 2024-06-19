def add(num1, num2, num3):
    result = num1 + num2 + num3
    print("result is: {}".format(result))

# add(10, 20, 30)
add(num1=10, num3=20, num2=30)


# Default Arguments/Inputs
def square(num=5):
    result = num * num
    print("result is: {}".format(result))

square()
square(3)
square(num=9)

# def subtract(num1=10, num2): # error
def subtract(num1, num2=10):
    result = num1 - num2
    print("result is: {}".format(result))

subtract(num1=10)