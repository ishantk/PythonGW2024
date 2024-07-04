numbers = list(range(10, 101, 10))
# numbers = tuple(range(10, 101, 10))
print("numbers is:", numbers)
print("numbers type is:", type(numbers))

numbers.append(99)
numbers.append(77)
numbers.append(103)
numbers.append(11)

print("numbers is:", numbers)
print("Len is:", len(numbers))
print("Sum is:", sum(numbers))
print("Min is:", min(numbers))
print("Max is:", max(numbers))
print("Avg is:", sum(numbers)/len(numbers))

# result = tuple(reversed(numbers))
result = list(reversed(numbers))
print("result is:", result)

# HW: reverse the below list using operators/for/if else/indexing etc...
#       0    1   2  3   4   5
data = [10, 20, 30, 40, 50, 30]
# data1 = []

# for idx in range(len(data)-1, -1, -1):
#     print(data[idx])
#     data1.append(data[idx])

# print(data1)


idx = data.index(40)
print("idx is:", idx)

result = data.count(30)
print("result is:", result)


c = 0
for idx in range(len(data)):
    if data[idx] == 30:
        c+=1

print("c is:", c)


data = [10, 30, 50, 20, 5, 19, 30]
names = ["john", "Abel", "jennie", "sia", "kim", "anna"]

data.sort()
print("data is:", data)
# Find how to sort in reverse order using the same sort function

names.sort()
print("names:", names)

print(min(names))
print(max(names))

names.remove("sia")
data.remove(30)

print("data is:", data)
print("names:", names)

data = [10, 20, 30, 40, 50]
data.pop()
data.pop(0)
data.clear()
print("data after pop:", data)

data = [10, 20, 30, 40, 50]
data.append(99)
data.insert(2, 77)
data.insert(-1, 88)

print("data is:", data)

# del data[1]
# del data[1:4]