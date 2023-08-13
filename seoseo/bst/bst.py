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

    def insert(self, value, node=None):
        if node is None:
            if self.root is None:
                self.root = TreeNode(value)
            else:
                self.insert(value, self.root)
        else:
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                else:
                    self.insert(value, node.left)
            else:
                if node.right is None:
                    node.right = TreeNode(value)
                else:
                    self.insert(value, node.right)

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

    def preorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=' ')
    
    def getMin(self, node=None):
        if node is None:
            node = self.root
        while node.left:
            node = node.left
        return node.value

    def getMax(self, node=None):
        if node is None:
            node = self.root
        while node.right:
            node = node.right
        return node.value
    
    def bfs(self):
        if self.root is None:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.value, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def existInTree(self, value, node=None):
        if node is None:
            node = self.root
            
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True
        return False


# Test the binary tree
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(97)
    tree.insert(32)
    tree.insert(2)
    tree.insert(12)
    tree.insert(46)
    tree.insert(6)
    tree.insert(58)


    print("Preorder Traversal:")
    tree.preorder()  # Output: 

    print("Inorder Traversal:")
    tree.inorder()  # Output: 

    print("Postorder Traversal:")
    tree.postorder()  # Output: 

    print("\nMinimum Value:", tree.getMin())  # Output: 2
    print("Maximum Value:", tree.getMax())  # Output: 97
    print("BFS Traversal:")
    tree.bfs()  # Output: 97 32 2 12 46 58 6

    n = 58
    print(f"Value {n} exists in the tree:", tree.existInTree(n))  # Output: True
    n = 100
    print(f"Value {n} exists in the tree:", tree.existInTree(n))  # Output: False
    n=2
    print(f"Value {n} exists in the tree:", tree.existInTree(n))  # Output: True

# End of the code
print()
printTime(start)
