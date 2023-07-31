import time
from collections import deque

start = time.time()  # Record the start time

def printTime(start):
    # Calculate the runtime by subtracting the current time from the start time
    print("Runtime:", time.time() - start)
    print()

# Implementation of the binary tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    # Recursive insertion into the binary tree
    # node == current node, value == the value to insert
    def _insert_recursive(self, node, value):
        if value < node.value:
            # Insert a new node to the left of the current node
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def bfs(self):
        if self.root is None:
            return

        q = deque([self.root])

        while q:
            curr = q.popleft()
            print(curr.value, end=' ')

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        print()

    def preorder(self, node=None):
        if node is None:
            node = self.root

        stack = [node]  # Use a stack to keep track of nodes

        while stack:
            current = stack.pop()
            print(current.value, end=' ')

            if current.right:  # Right child first to ensure left child is processed first (LIFO)
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        
        print()

    def inorder(self, node=None):
        if node is None:
            node = self.root

        stack = []
        current = node

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print(current.value, end=' ')
                current = current.right

        print()

    def postorder(self, node=None):
        if node is None:
            node = self.root

        stack1 = [node]
        stack2 = []

        while stack1:
            current = stack1.pop()
            stack2.append(current)

            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)

        while stack2:
            print(stack2.pop().value, end=' ')
        
        print()


# Test the binary tree
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)

    print("BFS Traversal:")
    tree.bfs()  # Output: 5 3 7 2 4 6 8

    print("Preorder Traversal:")
    tree.preorder()  # Output: 5 3 2 4 7 6 8

    print("Inorder Traversal:")
    tree.inorder()  # Output: 2 3 4 5 6 7 8

    print("Postorder Traversal:")
    tree.postorder()  # Output: 2 4 3 6 8 7 5

# End of the code
print()
printTime(start)
