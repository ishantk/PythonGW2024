"""
i:0             10, 30, 50, 20, 40
j:0-3 j: 0      10, 30, 50, 20, 40
j:0-3 j: 1      10, 30, 50, 20, 40
j:0-3 j: 2      10, 30, 20, 50, 40
j:0-3 j: 3      10, 30, 20, 40, 50


i:1             10, 30, 20, 40, 50
j:0-2 j:0       10, 30, 20, 40, 50
j:0-2 j:1       10, 20, 30, 40, 50
j:0-2 j:2       10, 20, 30, 40, 50

i:2             10, 30, 20, 40, 50
j:0-1 j:0       10, 30, 20, 40, 50
j:0-1 j:1       10, 20, 30, 40, 50

i:3             10, 30, 20, 40, 50
j:0   j:0       10, 30, 20, 40, 50

"""

def bubble_sort(data):
    for i in range(len(data)-1):
        print("i is:", i)
        for j in range(len(data)-i-1):
            print(j, end=" ")

            if data[j] > data[j+1]:
                print("Swapping {} with {}".format(data[j], data[j+1]))
                # Swap Operation
                data[j], data[j+1] = data[j+1], data[j]

        print()

numbers = [10, 30, 50, 20, 40]

print("UnSorted Numbers:")
print(numbers)
print("~~~~~~~~~~~~~~~~~~~~~")
bubble_sort(numbers)
print("Sorted Numbers:")
print(numbers)

# HW: Explore different sorting techniques