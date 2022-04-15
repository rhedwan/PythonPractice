def factorial(n):
    # Replace with your own code
    if n == 1:
        return 1
    if n < 0:
        return -1
    return n * factorial(n-1)
    

print(factorial(-3))
print(factorial(3))
print(factorial(12))