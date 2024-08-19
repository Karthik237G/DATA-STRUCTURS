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

