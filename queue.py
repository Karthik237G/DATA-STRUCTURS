import queue
q=queue.Queue
numbers=[10,2,30,40,500]
for i in numbers:
  q.put(i)
  
for i in numbers:
  print(q.get(i))

//dequeue

from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

class Stack:
  def __init__(self):
    self.items=[]
  def push(self,item):
    self.items.append(item)
  def dequeue(self):
    if not self.is_empty():
      return self.items.remove(20)
    else:
      return None
  def first(self):
    if not self.is_empty():
      return self.items[0]
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
p=stack.dequeue()
print(p)
q=stack.first()
print(q)
