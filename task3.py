import heapq

heap = []

print("Enter 10 integers to insert into Min Heap:")

for i in range(10):
    val = input(f"Enter value {i+1}: ")
    heapq.heappush(heap, val)

print("\nMin Heap structure (as list):")
print(heap)