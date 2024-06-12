def square_of_numbers(nums):
    print("1. nums is:", nums, id(nums)) 
    
    for idx in range(0, len(nums)):
        nums[idx] = nums[idx] * nums[idx]

    print("2. nums is:", nums, id(nums)) 


numbers = [10, 20, 30, 40, 50]
print("A. numbers is:", numbers, id(numbers)) 
print("A. numbers[0] hashcode:", id(numbers[0]))
square_of_numbers(numbers)
print("B. numbers is:", numbers, id(numbers))
print("B. numbers[0] hashcode:", id(numbers[0])) 
