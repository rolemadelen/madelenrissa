# Heap

Heap is a special tree-based data structure in which the tree is complete binary tree.

## Types of Heap

- Max-Heap - the key present at the root node must be **greatest** among the keys present at all of it's children.
- Min-Heap - the key present at the root node must be **smallest**.

Above property applies in all sub-trees as well.

## Properties of Heap

- Complete Binary Tree
- Heap property - root is the min/max element for Min Heap and Max Heap respectievly.
- Efficient insertion and deletion
- Efficient access to extremal elements - O(1)

## Operations

- `heapify` - a process of creating a heap from an array - O(logN)
- `insert` - insert an element in existing heap - O(logN)
- `delete` - delete max/min element in existing heap and reorganize the heap - O(logN)

## Advantages

- fast access to max/min element
- efficient insertion and deletion
- can be efficiently implemented as an array
- suitable for real-time applicationns

## Disadvantage

- not suitable for searching for an element other than max and min - O(N)
- extra memory overhead to maintain heap structure
- slower than other data structures like arrays and linked lists for non-priority queue operations
