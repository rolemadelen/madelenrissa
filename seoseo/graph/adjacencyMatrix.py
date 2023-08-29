import time
from collections import deque

start = time.time()  # Record the start time


def printTime(start):
    # Calculate the runtime by subtracting the current time from the start time
    print("Runtime:", time.time() - start)
    print()

# Implementation of the graph Adjacency Matrix


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


class GraphAdjacencyMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        # create 2d matrix that has every element is 0
        self.adj_matrix = [
            [0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, src_vertex, dest_vertex):
        if 0 <= src_vertex < self.num_vertices and 0 <= dest_vertex < self.num_vertices:
            # connection status with each node
            # undirected graph
            self.adj_matrix[src_vertex][dest_vertex] = 1
            self.adj_matrix[dest_vertex][src_vertex] = 1
            # for directed
            # self.adj_matrix[src_vertex][dest_vertex] = 1

    def get_adjacency_matrix(self):
        return self.adj_matrix


graph = GraphAdjacencyMatrix(5)

# adding Edge
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 3)
graph.add_edge(3, 4)

# Print near matrix
for row in graph.get_adjacency_matrix():
    print(row)

print('-'*20)
graph = GraphAdjacencyMatrix(num_vertices=4)
# adding Edge
graph.add_edge(src_vertex=0, dest_vertex=1)
graph.add_edge(src_vertex=0, dest_vertex=2)
graph.add_edge(src_vertex=1, dest_vertex=2)
graph.add_edge(src_vertex=1, dest_vertex=3)
graph.add_edge(src_vertex=2, dest_vertex=3)

# Print near matrix
for row in graph.get_adjacency_matrix():
    print(row)

# End of the code
print()
printTime(start)
