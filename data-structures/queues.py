##Simple queue and deuque implemetation

from collections import deque

queue=deque()

queue.append(1)
queue.append(2)

while len(queue)!=0:
    print(queue)
    queue.popleft()
    ## if we use queue.pop it will remove the last element of the queue and not the first one.
