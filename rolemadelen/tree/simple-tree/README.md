# Tree
- Tree is a non-linear data structure.
- Trees have a key and children.
- Tree Traversal: DFS (inorder, preorder, postorder) and BFS
- Recursive algorithms are commonly used with Trees
- In CS, Trees grow down.

## Terminology

```
        Fred
     /   |   \
  Kate  Jim Sally
 /  \
Sam Hugh
```

- **Root** - top node in the tree
  - Fred is the root
- **Child** - line down directly from a parent
  - Kate is a child of Fred
  - Fred is a parent of Kate
- **Ancestor** - parnt, or parent of parent, etc
  - Kate and Fred are ancestors of Sam
- **Descendant** - child, or child of child, etc
  - Kate, Jim, Sally, Sam, Hugh, are all descendants of Fred
- **Siblings** - sharing same parent
  - Sam and Hugh are sbilings
- **Leaf** - node with no children
  - Jim, Sally, Sam, Hugh are all leaf nodes
- **interior nodes** - Non-leaf
- **Level** - 1 + number of edges between root and node
  - Fred: Level 1
  - Kate and siblings: Level 2
  - Sam and Hugh: Level 3
- **Height** - max depth of subtree node and farthest leaf
  - Sam and Hugh: Height 1
  - Fred: Height 3
- **Forest** - collection of trees

## Node 
- key
- children: list of children nodes
- (optional) parent

## Nodes in Binary Tree
- key
- left
- right
- (opitonal) parent

## Traversal
- Depth-first - we completely traverse one sub-tree before exploring a sibling sub-tree.
  - inorder - (left, visit, right) traverse in alphabetical or numerical order for BST
  - preorder - (visit, left, right)
  - postorder - (left, right, visit)
- Breadth-first - We travelse all nodes at one level before progressing to the next level.
  - use Queue