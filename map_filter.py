numbers = [-12,34,252,45,25,22,5,252,234,525,2,52,34,2252,4412,0]
newNumber = list(map(lambda x: x**2, numbers))
print(newNumber)

evenNumber = list(filter(lambda x: x%2==0, numbers))
print(evenNumber)