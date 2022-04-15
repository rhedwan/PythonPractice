class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

def is_match(last, new):
    if last == "(" and new == ")":
        return True
    elif last == "{" and new == "}":
        return True
    elif last == "[" and new == "]":
        return True

def is_bracket_balance(brackets):
    stack = Stack()
    is_balanced = True
    start = 0 
    while start < len(brackets) and is_balanced:
        bracket = brackets[start]
        if bracket in "([{":
            stack.push(bracket)
            is_balanced = True
        else:
            if stack.is_empty():
                is_balanced = False
                break
            else:
                top = stack.pop()
                if not is_match(top, bracket):
                    is_balanced = False
                    break
        start += 1
    if stack.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_bracket_balance("[][]"))
print(is_bracket_balance("[([][]])"))
print(is_bracket_balance("[[]]"))
print(is_bracket_balance(""))