"""
    Multi Value Containers
        
    Sequences:    
        Tuple
        List
        String
        
    Set
    Dictionary


    Properties
     1. Indexing
     2. Negative Indexing
     3. Slicing
     4. Concatenation
     5. Multiplicity
     6. Memebership Testing
"""

# 1D List
# 1. Indexing 
# 2. Negative Indexing 
#           0   1   2
#          -3  -2  -1
my_data = (10, 20, 30)

# 2D List (List of Lists)
numbers = [
            [10, 20, 30],   # 0 -3
            [30, 40, 50],   # 1 -2
            [60, 70, 80]    # 2 -1
          ]

# 3D List (List of List of Lists)
large_data = [
                [
                    [10, 20, 30],   # 0 -3
                    [30, 40, 50],   # 1 -2                          0 -2
                    [60, 70, 80]    # 2 -1
                ],
                [
                    [140, 200, 30],         # 0 -3
                    [30, 40, 50, 60, 5],    # 1 -2                  1  -1
                    [60, 70]                # 2 -1
                ],
             ] 


            

print(my_data[0])
print(my_data[-1])
print(len(my_data))

print(numbers[0])
print(numbers[-1])
print(len(numbers))

print(large_data[0])
print(large_data[-1])
print(len(large_data))

print(large_data[1][0][0])
print(large_data[-1][-3][-3])

name = "Johns Cafe"
name = 'John\'s Cafe'
name = """Johns Cafe
Welcome to Cafeteria
Todays Menu:
Coffee
Burger
Cookie"""

print(name)
print(name[0])
print(name[-1])
print(name[-2])

# 3. Slicing
#  0                                    9
# -10                                  -1
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
data = list(range(10, 101, 10))
print("data is:")
print(data)

print("data[0:3]", data[0:3])
print("data[3:7]", data[3:7])
print("data[5:]", data[5:])
print("data[:4]", data[:4])

print("data[:-5]", data[:-5])
print("data[-5:-2]", data[-5:-2])

email = "john@example.com"
print("email[-4:]: ", email[-4:])
print("email[12:]: ", email[12:])

# 4. Concatenation
data1 = [10, 20, 30]
data2 = [40, 50, 60]

data3 = data1 + data2
print(data3)

# 5. Multiplicity
data4 = data1 * 3
print(data4)

prices = [100, 500, 700, 300]
prices1 = prices * 2
print(prices1)

# 6. Membership Testing
print(10 in prices)         # False
print(10 not in prices)     # True

quote = "Search the candle rather than cursing the darkness"
print(quote[6])

# Dictionary
student = {
    "rollno": 1,
    "name": "John",
    "age": 20,
    "gender": "male",
    "address": "redwood shores",
}

print("student[age]:", student["age"])

# Membership Testing works with keys
print(1 in student)
print("name" in student)
