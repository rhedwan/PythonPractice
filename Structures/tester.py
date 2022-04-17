class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    return self.items.append(item)

  def pop(self): 
    return self.items.pop()

  def is_empty(self):
    return self.items == []

  

def FirstReverse(strParam):
  print("saf")
  stack = Stack()
  str_ = ""
  print(strParam)
  for i in range(len(strParam)):
    print(strParam[i])
    stack.push(strParam[i])

  while not stack.is_empty():
    str_ += stack.pop()
  
  print(str_)
  return str_

print(FirstReverse("dfsfg"))