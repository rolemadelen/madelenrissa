# Tree

- [x] Intro to Trees (video)

- [x] Tree Traversal (video)
  - [x] Inorder
  - [x] Preorder
  - [x] Postorder
- [ ] Understand BFS (Breadth First Search)
- [ ] Understand DFS (Depth First Serach)

## Intro to Trees (video)
1. Hierarchy
  2. Empty or a node with a key and a list of child trees
  - Empty Tree : 
    1. Tree with one node:
      - Fred
    2. Tree with two node:
      - Fred
          | 
        Sally

  3. Terminology:
    - Root : Top node in the tree
    - A child has a line down directly from a parent
    - Ancestor : parent or parent of parent, etc.
    - Descendant : child, or child of child, etc. In verse of ancestor.
    - Sibling : sharing the same parent.
    - Leaf : Node with no children.
    - Interior Node( == non-leaf) : Node with children.
    - Level : 1 + num edges between root and node.
    - Height : A maximum depth o f subtree node and farthest leaf.
    - Forest : Collection of trees.
  
    - Node contains : 
      - key
      - children : list of children nodes
      - (optional) parent

  - Binary Tree : 
    - node contains : 
      - key
      - left 
      - right
      - (optional) parent
  
  - Height(tree) : 
    ```
    if tree == nil:
      return 0
    return 1 + Max(Height(tree.left), Height(tree.right))
    ```
  
  - Size(tree):
    ```
    if tree == nil:
      return 0
    return 1 + Size(tree.left) + Size(tree.right)
    ```

## Tree Traversal (video)
=> Visiting all the nodes of tree.
- Depth First
  - inOrderTraversal(tree):
    ```
    if tree == null:
      return 
    InOrderTraversal(tree.left)
    Print(tree.key)
    InOrderTraversal(tree.right)
    ```
    - binary tree
    - Les - Cathy -> **Alex** -> **Cathy** -> **Frank** -> **Les** -> **Nancy** -> **Sam** -> **Tony** -> **Violet** -> **Wendy**    
  - preOrderTraversal(tree):
    ```
    if tree == null:
      return 
    Print(tree.key)
    preOrderTraversal(tree.left)
    preOrderTraversal(tree.right)
    ```
    - general trees
    - **Les** - **Cathy** -> **Alex** -> Cathy -> **Frank** -> Cathy -> Les -> **Sam** -> **Nancy** -> Sam -> **Violet** -> **Tony** -> Violet -> **Wendy** 
    - preOrderTraversal is also called as DFT(Depth-First Traversal).
    <img width="240" alt="https://yoongrammer.tistory.com/70" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FqaUdk%2Fbtq16y96ZK5%2FHzgM9ijvptwnj6jxshGYbK%2Fimg.png">
    - A→B→D→E→C→F→G

  - postOrderTraversal(tree):
    ```
    if tree == null:
      return 
    postOrderTraversal(tree.left)
    postOrderTraversal(tree.right)
    Print(tree.key)
    ```
    - Les - Cathy -> **Alex** -> Cathy -> **Frank** -> **Cathy** -> Les -> **Sam** -> **Nancy** -> Sam -> **Violet** -> **Tony** -> violet -> **Wendy**

- Breadth-first
  - LevelTraversal(tree)
    ```
    if  tree == nil : return
    Queue q
    q.enqueue(tree)
    while not q.Empty():
      node <- q.Dequeue()
      Print(node)
      if node.left != nil:
        q.Enqueue(node.left)
      if node.right != nil:
        q.Enqueue(node.right)
    ```

- Summary
  - Trees are used for lots of different things
  - Trees have a key and children
  - Tree walks : DFS, BFS
  - when working with a tree, recursive algorithms are common

## Implement

- [x] Inorder
- [x] Preorder
- [x] Postorder
  

## Understand BFS (Breadth First Search)
- We traverse all nodes at one level before progressing to the next level.

## Understand DFS (Depth First Serach)
- We completely traverse one sub-tree before exploring a sbiling sub-tree

