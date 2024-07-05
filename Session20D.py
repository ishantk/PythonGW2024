quote = "Be Exceptional"
print(quote[len(quote)-1])

message = "Hello, how are you. I hope you are doing good"
words = message.split(" ")
print(words)

names = "john, jennie, jim, jack, joe"
words = names.split(", ")
print(words)
print(type(words))

file = open("quotes.txt", "r")
# print(len(file.read().split(" ")))
lines = file.readlines()
print(lines)

# In future, we will write more short code :)
# List Comprehension :)
# map, fiter and reduce

total_words = 0
for line in lines:
    total_words += len(line.split(" "))
    

print("total_words", total_words)