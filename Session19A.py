# Explore SET
# Unique

john_followers = {"fionna", "sia", "jack", "joe", "george", "kia"}
print(john_followers)
print(type(john_followers))
print(len(john_followers))

numbers = list(range(10, 101, 10))
numbers1 = set(numbers)
print("numbers:", numbers)
print("numbers1:", numbers1)

numbers1.add(101)
numbers1.add(201)
numbers1.add(301)

print("numbers1:", numbers1)
# numbers1.pop()
# numbers1.pop()
# print("numbers1:", numbers1)

print("1. numbers1:", numbers1)
numbers1.remove(90)
numbers1.remove(30)
numbers1.remove(101)
numbers1.discard(201)
print("2. numbers1:", numbers1)

john_followers = {"fionna", "sia", "jack", "joe", "george", "kia"}
jake_followers = {"anna", "sia", "kia"}
fionna_followers = {"sia", "joe"}

mutual_followers = john_followers.intersection(jake_followers)
print(mutual_followers)

result = fionna_followers.issubset(john_followers)
print("result is:", result)

result = john_followers.issuperset(fionna_followers)
print("result is:", result)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Error
# C = A + B
# print("C is:", C)

D = A - B
print("D is:", D)

E = A ^ B
print("E is:", E)

F = A | B
print("F is:", F)


A.clear()
print("A is:", A)
print("Length of A is:", len(A))

# Create an Empty Set
my_set = set()
my_list = []
my_dict = {}