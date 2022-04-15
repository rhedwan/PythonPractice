class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()
        
    def get_items(self):
        return self.items

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

def convert_int_to_bin(dec_num):
    checker = True
    stack = Stack()
    new_dec_num = dec_num
    if dec_num == 0 or dec_num == 1:
        return dec_num

    while checker:
        remainder = new_dec_num % 2 
        if remainder == 1 or remainder ==0:
            stack.push(remainder)

        new_dec_num = int(new_dec_num / 2)
        if new_dec_num == 1 :
            stack.push(new_dec_num)
            checker = False
            break
    binary_number = ""
    while not stack.is_empty():
        binary_number += str(stack.pop())

    return  binary_number

print(convert_int_to_bin(242))
print(convert_int_to_bin(2))
print(convert_int_to_bin(20))
print(convert_int_to_bin(3))
print(convert_int_to_bin(4))
print(convert_int_to_bin(0))
print(convert_int_to_bin(1))