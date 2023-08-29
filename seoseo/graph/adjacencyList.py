import time
from collections import deque

start = time.time()  # Record the start time


def printTime(start):
    # Calculate the runtime by subtracting the current time from the start time
    print("Runtime:", time.time() - start)
    print()

# Implementation of the graph Adjacency List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get_values(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


class GraphAdjacencyList:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [LinkedList() for _ in range(num_vertices)]

    def add_edge(self, src_vertex, dest_vertex):
        if 0 <= src_vertex < self.num_vertices and 0 <= dest_vertex < self.num_vertices:
            # undirected graph
            linked_list1 = self.adj_list[src_vertex]
            linked_list1.append(dest_vertex)

            linked_list2 = self.adj_list[dest_vertex]
            linked_list2.append(src_vertex)

    def get_neighbors(self, vertex):
        if 0 <= vertex < self.num_vertices:
            return self.adj_list[vertex].get_values()
        else:
            return []


graph = GraphAdjacencyList(5)

# adding Edge
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 3)
graph.add_edge(3, 4)

# Check neighbor Edge
print(graph.get_neighbors(0))  # [1, 4]
print(graph.get_neighbors(3))  # [1, 4]

graph = GraphAdjacencyList(num_vertices=4)
# adding Edge
graph.add_edge(src_vertex=0, dest_vertex=1)
graph.add_edge(src_vertex=0, dest_vertex=2)
graph.add_edge(src_vertex=1, dest_vertex=2)
graph.add_edge(src_vertex=1, dest_vertex=3)
graph.add_edge(src_vertex=2, dest_vertex=3)

# Print neighbors
for i in range(graph.num_vertices):
    print(f"Node {i}'s neighbors: {graph.get_neighbors(i)}")

# End of the code
print()
printTime(start)
