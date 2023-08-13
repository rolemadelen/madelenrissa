# Binary Search Tree (BST)

- Implement
  - [X] insert(value)
- DFS(Depth First Serach)
  - [x] inorder()
  - [x] preorder()
  - [x] postorder()
- [x] getMin()
- [x] getMax()
- [x] bfs() -- print values in level order
- [x] existInTree(value)

## Binary Search Tree (BST)
- A Binary Search Tree is a type of binary tree that adheres to the following conditions for each node:
  - All the nodes in the left subtree have values less than the value of the current node.
  - All the nodes in the right subtree have values greater than the value of the current node.





## Why using queue in BFS?
- The reason for using a queue in BFS (Breadth-First Search) is to visit nodes in level order. A queue operates based on the First-In-First-Out (FIFO) principle, which allows us to visit nodes on the same level in order while maintaining the order of nodes. During the BFS algorithm, we enqueue the children of the visited nodes. By using a queue, transitioning to the next level happens naturally after visiting all nodes at one level. This is thanks to the queue's FIFO principle. When visiting nodes, we visit the node at the front of the queue and add its children to the end of the queue. Thus, by visiting nodes in the queued order, we can move to the next level. If we were to use a data structure following the Last-In-First-Out (LIFO) principle, such as a stack, it would be difficult to maintain the node order, making it challenging to perform the search in level order. For these reasons, a queue is utilized in BFS to efficiently manage the nodes and preserve the visiting order.