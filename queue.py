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

class Queue:
  def __init__(self):
    self.items=[]
  def push(self,item):
    self.items.append(item)
  def dequeue(self):
    if not self.is_empty():
      return self.items.pop(0)
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

queue=Queue()
queue.push(10)
queue.push(20)
queue.push(40)
queue.push(50)
queue.push(70)
queue.push(50)
queue.push(270)
queue.push(202)
print(queue)
p=stack.dequeue()
print(p)
q=queue.first()
print(q)
