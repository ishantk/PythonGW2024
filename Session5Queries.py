# Elevator Problem

floors = 10

floor = 0 # 0th or default floor

floor_to_go = int(input("Enter Floor Number to Go: "))

"""
while floor <= floors:
    print("At Floor Number:", floor)

    if floor_to_go == floor:
        print("You have Reached at Floor Number:", floor)
        break

    floor += 1
"""


for floor in range(0, 11):
    print("At Floor Number:", floor)

    if floor_to_go == floor:
        print("You have Reached at Floor Number:", floor)
        break