from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue.popleft())
print(queue.pop())

print(queue)

if not queue:
    print("Empty queue")
else: 
    print("There are some elements left")