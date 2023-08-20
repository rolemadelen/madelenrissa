# Heap

- Implement with Binary Tree
  - [x] min-heap
  - [x] max-heap
  - [x] insert : adjusted within the heap structure to maintain heap conditions
  - [x] search next empty position
  - [x] find the parent node
  - [x] finds and returns the node number
  - [x] find the node at a specific node number
  - [x] unheap : adjusting within the heap structure to maintain heap conditions


- Implement with Array
  - [ ] min-heap
  - [ ] max-heap

## Heap
- Heap is a data structure that represents a complete binary tree, storing nodes in a sorted order. There are primarily two types of heaps, each satisfying a specific condition:
  - Max Heap: Each parent node's value is greater than or equal to its children's values. This ensures that the maximum value is located at the root node.
  - Min Heap: Each parent node's value is less than or equal to its children's values. Consequently, the minimum value is located at the root node.
- Heaps are filled level by level, allowing for their implementation using arrays too. Typically, an array with indices starting at 1 is used, where the left child of a node with index i is at 2i, the right child is at 2i + 1, and the parent node is at i / 2 (integer division). Using an array results in a space complexity of O(N).
- Heaps are utilized in applications like priority queues, Dijkstra's algorithm, and heapsort, providing efficient time and space complexity for these use cases.


## Time Complexity of Heap
1. Insertion: The operation of adding a node to the heap and reordering it to meet the conditions has a time complexity of O(log N), as the inserted node can traverse the height of the heap.
2. Deletion: The operation of deleting the root node (maximum or minimum value) and reordering it to meet the constraints has a time complexity of O(log N), as the last node is removed and traverses the height of the tree.
3. Search: To find the maximum value in a max heap or the minimum value in a min heap, the time complexity is O(1), as the values are located at the root node.

