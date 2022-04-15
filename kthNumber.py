# print({(24,4), 9})

def result(k):
    # print({[24,4], 9})
    me  = [34, 2, 5, 45, 52, 245]
    me.sort()
    # print(me)
    return me[-k]

print(result(2))
print(result(1))
print(result(4))
print(result(6))