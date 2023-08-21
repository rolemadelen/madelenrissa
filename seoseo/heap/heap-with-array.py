import heapq
import time
start = time.time()  # Record the start time


def printTime(start):
    # Calculate the runtime by subtracting the current time from the start time
    print("Runtime:", time.time() - start)


print()

# Implementation of the binary tree


class Heap:
    def __init__(self):
        self.data = []

    def push(self, x):
        heapq.heappush(self.data, x)

    def pop(self):
        return heapq.heappop(self.data)


class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def push(self, x):
        super().push(x)

    def pop(self):
        return super().pop()


class MaxHeap(Heap):
    def __init__(self):
        super().__init__()

    def push(self, x):
        super().push(-x)

    def pop(self):
        return -super().pop()


# End of the code
print()
printTime(start)


def main():
    # Min Heap example
    min_heap = MinHeap()
    values = [50, 30, 40, 10, 20, 60]

    print("Insertion order for nodes in Min Heap:")
    for value in values:
        min_heap.push(value)
        print(value, end=' ')
    print()

    # Find minimum value in Min Heap
    min_value = min_heap.pop()
    print("Root node value for Min Heap:", min_value)

    # Max Heap example
    max_heap = MaxHeap()

    print("\nInsertion order for nodes in Max Heap:")

    for value in values:
        max_heap.push(value)
        print(value, end=' ')
    print()

    # Find maximum value in Max Heap
    max_value = max_heap.pop()
    print("Root node value for Max Heap:", max_value)


if __name__ == "__main__":
    main()
