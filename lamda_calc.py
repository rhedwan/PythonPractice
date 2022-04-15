add = lambda n1, n2: n1 + n2
subtract = lambda n1, n2: n1 - n2
multiply = lambda n1, n2: n1 * n2
divide = lambda n1, n2: n1 / n2

def calculator(operation, n1, n2):
    return operation(n1, n2)

print(calculator(add, 543, 3453))
print(calculator(multiply, 543, 3453))
print(calculator(subtract, 54302, 3453))
print(calculator(divide, 543, 34))