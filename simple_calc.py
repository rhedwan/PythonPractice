def add(n1, n2):
    return f"The addition of {n1, n2} is {n1 + n2}"

def multiply(n1, n2):
    return f"The multiply of {n1, n2} is  {n1 * n2}"

def divide(n1, n2):
    return f"The division of {n1, n2} is {n1 / n2}"

def subtract(n1, n2):
    return f"The subtraction of {n1, n2} is {n1 * n2}"

def calculator(operation, num1, num2):
    return operation(num1, num2)

print(calculator(add, 23, 344))
print(calculator(multiply, 23, 344))
print(calculator(divide, 23343, 344))
print(calculator(subtract, 23, 344))
