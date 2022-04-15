from inspect import stack


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    
def string_reverse(string):
    stack = Stack()
    start , start_ = 0 , 0
    reversed_str = ""
    while start < len(string):
        index = string[start]
        stack.push(index)
        start += 1
    while start_ < len(string):
        reversed_str += stack.pop()
        start_ += 1
    return reversed_str

print(string_reverse("Bankole"))
print(string_reverse("Hello"))
print(string_reverse("!evitacudE ot emocleW"))