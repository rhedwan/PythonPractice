def count_low_high(num_list):
    count_high = 0
    count_low = 0
    tracker = []
    if len(num_list) == 0:
        return None

    for i in num_list :
        if i > 50 or i % 3 == 0:
            count_high += 1
        else:
            count_low += 1


    tracker.extend([count_low, count_high])
    return tracker

print(count_low_high([20, 9, 51, 81, 50, 42, 77]))
print(count_low_high([]))

def count_low_high_lambda(num_list):
    if len(num_list) == 0:
        return None
    high_list = list(filter(lambda x: x > 50 or x % 3 == 0, num_list ))
    low_list = list(filter(lambda x:not (x > 50 or x % 3 == 0), num_list ))
    return [len(low_list), len(high_list)]

print(count_low_high_lambda([20, 9, 51, 81, 50, 42, 77]))
print(count_low_high_lambda([]))