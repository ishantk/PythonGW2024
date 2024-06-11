# What is a Function/Method/Procedure
# A function is a piece of code, which we use again and again
# It can have input, which is processed and you get an output

# f(x) = y
# where y is: x*x + 1
# x: 1 => 2
# x: 3 => 10


def f(x):
    y = x*x + 1
    print("y is:", y)

f(1)
f(2)
f(3)
f(5)


def whole_square(a, b):
    result = a*a + b*b + 2*a*b
    print("result is:", result)

whole_square(2, 5)
whole_square(a=5, b=4)