def counts(n):
    print(n)
    if n == 0:
        return 0
    counts(n-1)

counts(10)
