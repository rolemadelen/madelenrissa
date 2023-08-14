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


## Time Complexity of BST
1. Average : O(log N)
2. Worst : O(H) == O(N)
  - Worst case could be the shape of the tree looks like linked-list. H as Height and N represents the number of Nodes in the tree, and the height of the tree becomes equal to the number of nodes.
3. getMin, getMax : O(N) 


### inorder, preorder, postorder -> to remember
- inorder : left subtree - current node - right subtree -> In my case I rememberd as start from left children tree to parent node and goes to right children tree. If node is not None. It recursive or using stack.
- preorder : current node - left subtree - right subtree -> If current Node is not None, process the current. Call or recursive to left subtree then process right subtree. It's sueful for finding a path
- postorder : left subtree - right subtree - current node -> If current Node is not None. This one is processing from the both subtree to parent node.

