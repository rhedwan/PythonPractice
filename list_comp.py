# List comprehension
nums = [10, 20, 30, 40, 50]
numSquareList = [i**2 for i in nums if i % 4 == 0 ]
print(numSquareList)


list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 == 100]

print(sum_list)