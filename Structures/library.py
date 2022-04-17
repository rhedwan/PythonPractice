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


def library(str):
    pass

