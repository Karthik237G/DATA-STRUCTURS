class Stack:
  def __init__(self):
    self.items=[]
  def push(self,item):
    self.items.append(item)
  def pop(self):
    if not self.is_empty():
      return self.items.pop()
    else:
      return None
  def peek(self):
    if not self.is_empty():
      return self.items[-1]
  def is_empty(self):
    return len(self.items) ==0
  def __len__(self):
    return len(self.items)
  def __str__(self):
    return str(self.items)

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(40)
stack.push(50)
stack.push(70)
stack.push(50)
stack.push(270)
stack.push(202)
print(stack)
p=stack.pop()
print(p)
q=stack.peek()
print(q)
