def fib(n):
    n1, n2= 0, 1
    count = 3
    if n <= 0:
        return -1
    if n == 1:
        return n1
    if n == 2:
        return n2
    while count <= n :
        nth = n1 + n2
        n1 = n2
        n2 = nth
        # print(n1,n2,nth)
        count += 1
    return nth

# print(fib(7))
print(fib(5))
# print(fib(1))
# print(fib(10))