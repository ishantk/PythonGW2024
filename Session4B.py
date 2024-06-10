# Bitwise Operators
# &, |, ^

num1 = 10   # 1 0 1 0
num2 = 8    # 1 0 0 0

print("num1 in binary is:", bin(num1))
print("num2 in binary is:", bin(num2))

result1 = num1 & num2 # 1 0 0 0 -> 8
result2 = num1 | num2 # 1 0 1 0 -> 10
result3 = num1 ^ num2 # 0 0 1 0 -> 2

print("result1:", result1)
print("result2:", result2)
print("result3:", result3)

# Shift Operators
# >>, <<

num1 = 8
num2 = 3
#           8  >>  3
result1 = num1 >> num2 # 8 // 2 power 3
print("result1 right shift is:", result1)

number = result1 << num2
print("number is:", number)

#           8  <<  3
result2 = num1 << num2 # 8 * 2 power 3
print("result1 left shift is:", result2)

number = -13 # 1 0 1 1
result = number >> 2
print(number, ">> 2 is:", result)

#   11
#   0 0 0 0  1 0 1 1
#   >> 2
#   _ _ 0 0  0 0 1 0 -> 2
#   0 0 0 0  0 0 1 0 -> 2

#   -11
#  0 0 0 0  1 0 1 1
#  1 1 1 1  0 1 0 0
#                 1
#  1 1 1 1  0 1 0 1
#  >> 2
#  _ _ 1 1  1 1 0 1
#  1 1 1 1  1 1 0 1
#  0 0 0 0  0 0 1 0
#                 1
#  0 0 0 0  0 0 1 1 -> -3

#  13
#  0 0 0 0   1 1 0 1
#  >> 2
#  _ _ 0 0   0 0 1 1 -> 3

#  -13
#  0 0 0 0   1 1 0 1
#  >> 2
#  _ _ 0 0   0 0 1 1 -> 3




