# Priority Queue

- Implement
  - Understand what PQ is.

## Priority Queue
- A priority queue is a data structure that stores data while assigning a priority to each data. The data with the highest priority is extracted first. Unlike a regular queue, data is stored in a way that it is sorted according to its priority when added. This means that the highest priority tasks or important data are processed first, which can be useful in various situations.

## Time Complexity of Priority Queue
- Array based: 
  - enqueue : Adding the new element at the last of the array -> O(1)
  - dequeue : Searching the minimum element in the array and delete and pulling the one each to in front -> O(N)

- Heap based:
  - enqueue: Inserting a new element into the heap and adjusting the tree to maintain the heap property takes time proportional to the height of the heap. -> O(log N)
  - dequeue: Removing the minimum (or maximum) element from the heap and same process for adjusting the tree. -> O(log N)

- Sequential or Linked List based:
  - enqueue & dequeue : Finding or adjusting the appropriate position based on priority requires O(N) in average.