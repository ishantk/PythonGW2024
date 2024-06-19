def add(num1, num2):
    sum = num1 + num2 + 10
    return sum

def square(num):
    return num * num

hello = add

def hello(num1, num2):
    result = num1 + num2 - 2
    return result

def add(num):
    return num*2

square = hello
hello = add

result = hello(num=5)
print("result is:", result)