

def get_max(data, length):
    # data, length belongs to get_max frame
    if length == 1:
        return data[0]
    else:
        previous = get_max(data, length-1)
        current = data[length-1]

        if previous > current:
            return previous
        else:
            return current


# numbers, max belongs to main frame
numbers = [10, 20, 30]
max = get_max(numbers, len(numbers))
print("Max is:", max)






"""
numbers = [1, 3, 5]

max = numbers[0]

for idx in range(1, len(numbers)):
    if numbers[idx] > max:
        max = numbers[idx]


print("Max is:", max)
"""