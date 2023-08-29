# Graph

- Implement with liked-list
  - [x] Adjacency List
    - add_edge
    - get_neighbors
  - [x] Adjacency Matrix
    - add_edge
    - get_adjacency_matrix

## Graph
- A graph consists of nodes (or vertices) and edges that connect them.
- Nodes represent individual items in the graph, and edges represent the connections or relationships between such items.
  - If the edges have a direction, it is called a 'directed graph', and if not, it's an 'undirected graph'. 
  - When weights are assigned to the edges it is referred to as a 'weighted graph'.
- Adjacency List : In this representation, each node keeps a list of the nodes to which it is directly connected. This list could be implemented as an array or a linked list. The adjacency list is more memory efficient, but it requires a time complexity of O(V) to check the connection between two nodes (V is the number of vertices in the graph).
- Adjacency Matrix : In Adjacency Matrix, the graph is represented as a 2D array of size VxV (V is the number of vertices in the graph). Each element in the matrix indicates whether a particular pair of nodes is connected. The adjacency matrix requires a time complexity of O(1) to check the connection between two nodes, but it consumes more memory.

### Adjacency List
- Using vertex as key.
- Memory efficiency. Save it when actually Edge exist.

### Adjacency Matrix
-  If indices i and j are connected, then matrix[i][j] = 1; otherwise, matrix[i][j] = 0.
- Although it stores information for all possible edges, resulting in higher memory usage, determining the connection between two vertices can be achieved in constant time.
## Time Complexity of Graph
- The time complexity of a graph typically depends on the number of nodes and edges in the graph.
  - Depth-First Search (DFS) and Breadth-First Search (BFS) have a time complexity of O(V + E), where V is the number of vertices (nodes), and E is the number of edges.
  - Shortest path algorithms like Dijkstra's algorithm can have a time complexity as low as O((V + E) log V), when using a heap.


