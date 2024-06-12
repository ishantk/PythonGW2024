# Nested Loops

black_square = "\u25A1"
white_square = "\u25A0"

# print(black_square)
# print(white_square)

for i in range(0, 8): # 0, 1, and 3
    # print("i is:", i)

    for j in range(0, 8): # 0, 1, 2, 3, 4
        # print(j, end=" # ")

        if i % 2 == 0:
            # print(j%2, end=" ")
            if j%2 == 0:
                print(black_square, end=" ")
            else:
                print(white_square, end=" ")
        else:
            # print((j+1)%2, end=" ")
            if (j+1)%2 == 0:
                print(black_square, end=" ")
            else:
                print(white_square, end=" ")

    print()

"""
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
"""

# HW: Place King and Queen on their right positions
#     Place Knights