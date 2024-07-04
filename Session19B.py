"""
Empty Structures:

my_tuple = ()
my_tuple = tuple()

my_list = []
my_list = list()

my_set = set()

my_dict = {}
my_dict = dict()
"""

# Explore Dictionary/Map/JSON

my_data = {
    101: "John",
    201: "Jennie",
    501: "Sia",
    99: "Joe",
    25: "Kim",
    201: "Anna"
}

# my_data = {
#     "jo": "John",
#     "je": "Jennie",
#     "si": "Sia",
#     "ji": "Joe",
#     "ki": "Kim"
# }

print("my_data")
print(my_data)

print(len(my_data))
print(min(my_data))
print(max(my_data))
print(sum(my_data)) # -> works only for int keys

print(my_data[201])
print(my_data.get(201))

my_data.pop(25)
# del my_data[25]

my_data[99] = "Joseph"
print(my_data)

attendance = ["june", "july", "aug", "july"]
college_attendance = {}.fromkeys(attendance, 100)
college_attendance["aug"] = 70
print(college_attendance)

items = list(my_data.items())
values = list(my_data.values())

print(items)
print(values)

for item in my_data.items():
    print(item)

for value in my_data.values():
    print(value)

my_data[333] = "harry"