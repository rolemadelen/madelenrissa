from queue import Queue
import time
from collections import deque

start = time.time()  # Record the start time


def printTime(start):
    # Calculate the runtime by subtracting the current time from the start time
    print("Runtime:", time.time() - start)
    print()


# Implementation of binary tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # None if there is no left child
        self.right = None  # None if there is no right child


class Heap:
    def __init__(self, comparator):
        # A variable that stores the root node of the heap. Initially, it is empty and set to None.
        self.root = None
        # A variable that stores the last node in the heap. Initially, it is empty and set to None.
        self.last_node = None
        # A variable that stores the number of nodes in the heap. Initially, there are no nodes, so it is set to 0.
        self.node_count = 0
        # A variable that stores a function to compare the values of two nodes. This function is necessary to implement either a Min Heap or a Max Heap.
        self.comparator = comparator

    # The inserted node is adjusted within the heap structure to maintain heap conditions.
    def insert(self, value):
        new_node = TreeNode(value)
        self.node_count += 1
        if not self.root:
            self.root = new_node
            self.last_node = new_node
        else:
            parent, is_left = self._next_empty_position()
            if is_left:
                parent.left = new_node
            else:
                parent.right = new_node

            self.last_node = new_node
            self._upheap(new_node)

    # finds the next empty position in the heap. The heap is a complete binary tree, so the node insertion space is determined by finding an empty space level-by-level.
    def _next_empty_position(self):
        if not self.root:
            return None, None

        node_count = self.node_count
        q = deque()
        q.append((self.root, 1))

        while q:
            node, node_number = q.popleft()
            if 2 * node_number > node_count:
                return node, True
            elif 2 * node_number + 1 > node_count:
                return node, False

            if node.left:
                q.append((node.left, 2 * node_number))
            if node.right:
                q.append((node.right, 2 * node_number + 1))

        return None, None

    # find the parent node of a given node.
    def _find_parent(self, node):
        if not self.root or self.root == node:
            return None

        node_number = self._find_node_number(node)
        parent_number = node_number // 2
        return self._find_node_by_number(parent_number)

    # finds and returns the node number of the given target_node. This method can be used to identify the position of a specific node.
    def _find_node_number(self, target_node):
        if not self.root:
            return 0

        current_number = 1
        q = deque()
        q.append((self.root, current_number))

        while q:
            node, node_number = q.popleft()
            if node == target_node:
                return node_number

            if node.left:
                q.append((node.left, 2 * node_number))
            if node.right:
                q.append((node.right, 2 * node_number + 1))

        return 0

    # finds and returns the node corresponding to the given target_number. This method can be used to find the node at a specific node number.
    def _find_node_by_number(self, target_number):
        if not self.root:
            return None

        current_number = 1
        q = deque()
        q.append((self.root, current_number))

        while q:
            node, node_number = q.popleft()
            if node_number == target_number:
                return node

            if node.left:
                q.append((node.left, 2 * node_number))
            if node.right:
                q.append((node.right, 2 * node_number + 1))

        return None

    # adjusts a specified node to satisfy the heap conditions. The inserted node's value is swapped with the parent node's value until the node value is greater than the parent value(== Max Heap) or the node value is smaller than the parent value(== Min Heap)
    def _upheap(self, node):
        while node:
            parent = self._find_parent(node)
            if parent and self.comparator(node.data, parent.data):
                parent.data, node.data = node.data, parent.data
                node = parent
            else:
                break

# inherit from the Heap class and are implemented to function as a min heap and max heap, respectively.


class MinHeap(Heap):
    # MinHeap class performs a switch only when the child data is smaller than the parent data.
    def __init__(self):
        super().__init__(lambda child_data, parent_data: child_data < parent_data)


class MaxHeap(Heap):
    # MaxHeap class performs a switch only when the child data is larger than the parent data.
    def __init__(self):
        super().__init__(lambda child_data, parent_data: child_data > parent_data)


# End of the code
print()
printTime(start)


def main():
    # Min Heap example
    min_heap = MinHeap()
    values = [50, 30, 40, 10, 20, 60]

    print("Insertion order for nodes in Min Heap:")
    for value in values:
        min_heap.insert(value)
        print(value, end=' ')
    print()

    root = min_heap.root
    if root:
        print("Root node value for Min Heap:", root.data)
    else:
        print("Min Heap is empty.")

    # Max Heap example
    max_heap = MaxHeap()

    print("\nInsertion order for nodes in Max Heap:")

    for value in values:
        max_heap.insert(value)
        print(value, end=' ')
    print()

    root = max_heap.root
    if root:
        print("Root node value for Max Heap:", root.data)
    else:
        print("Max Heap is empty.")


if __name__ == "__main__":
    main()

# delete 기능 구현하기
