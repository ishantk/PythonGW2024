# When you need to pass variable input to function (i.e 1 number or n numbers)
def add(*args):
    print(args)
    data = list(args)
    print(data)
    print(type(args))
    print(type(data))


add(10, 20, 30, 40, 50, "hi", "john", "hello")


print("=======================")

def numbers(**kwargs):
    print(kwargs)
    print(type(kwargs))


numbers(a=10, b=20, c=30)

def fun(*args, **kwargs):
    print(args)
    print(kwargs)


fun(10, 20, 30, 40, 50, "hi", "john", "hello", a=10, b=20, c=30)