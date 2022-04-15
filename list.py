# Using Trad. for loop
nums = [10, 20, 30, 40, 50]
nums_square = []
for i in nums:
    nums_square.append(i**2)

print(nums)
print(nums_square)

# Using while loop
init = 0 
numSquare = []
while init < len(nums_square):
    numSquare.append(nums[init]**2)
    init += 1

print(numSquare)

# Using built-in map
nums_square_ = list(map(lambda x: x**2, nums))
print(nums_square_)


# List comprehension
numSquareList = [i**2 for i in nums]
print(numSquareList)