file = open("customers.csv", "r")
# data = file.read()

lines = file.readlines()

print("File Data:")
print(lines)

for i in range(len(lines)):
    print(lines[i])