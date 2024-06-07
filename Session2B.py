john_friends = {"joe", "jim", "fionna", "harry", "kim", "joe"}
sia_friends = {"joe", "george", "fionna", "leo", "jack", "ben"}

print(john_friends)
print(sia_friends)

mutual_friends = john_friends & sia_friends

print(mutual_friends)

# Error: Set does not support indexing. It works on Hashing
# print(john_friends[0])
# Hence, we cannot get the data from Set