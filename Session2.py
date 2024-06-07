numbers = [10, 20, 30, 40, 50]
print(numbers, type(numbers), id(numbers))

# REFERENCE COPY Operation -> Copy the hashcode
my_numbers = numbers

print(my_numbers, type(my_numbers), id(my_numbers))

print(id(numbers[2]))
numbers[2] = 1122
print(id(numbers[2]))  


print(numbers)       
print(my_numbers)  

del numbers
print(my_numbers)
# print(numbers) # error