import queue
q=queue.Queue
numbers=[10,2,30,40,500]
for i in numbers:
  q.put(i)
  
for i in numbers:
  print(q.get(i))

