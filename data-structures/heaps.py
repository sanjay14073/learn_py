import heapq

heap = []  # Correct way to define a heap

heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

while len(heap) != 0:
    print(heap)
    heapq.heappop(heap)

# Notes:
# 1. Using heap.pop() removes the *last* element, not the smallest (i.e., not the heap root).
# 2. heapq is a *min-heap* by default.
# 3. To simulate a *max-heap*, insert elements as -x and multiply by -1 again when popping.
