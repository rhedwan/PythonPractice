def check_sum(num_list):
    found = False
    for num in num_list:
        for num_ in num_list:
            if num + num_ == 0:
                found =True
                break
    return found

print(check_sum([10, -14, 26, 5, -3, 13, -5]))
print(check_sum([10, -14, 26, 4, -3, 13, -5]))