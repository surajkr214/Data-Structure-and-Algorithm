# Graphs

## Overview
A graph is a non-linear data structure consisting of vertices (nodes) and edges (connections between nodes).

## Key Terms
- **Vertex/Node**: A point in the graph
- **Edge**: Connection between two vertices
- **Directed Graph**: Edges have direction (A → B)
- **Undirected Graph**: Edges have no direction (A ↔ B)
- **Weighted Graph**: Edges have weights/costs
- **Cycle**: Path that starts and ends at same vertex
- **Connected Graph**: Path exists between any two vertices
- **Degree**: Number of edges connected to a vertex

## Graph Representations

### 1. Adjacency Matrix
- 2D array where matrix[i][j] = 1 if edge exists
- **Space**: O(V²)
- **Edge lookup**: O(1)
- Good for dense graphs

### 2. Adjacency List
- Array of lists, each list contains neighbors
- **Space**: O(V + E)
- **Edge lookup**: O(degree)
- Good for sparse graphs

### 3. Edge List
- List of all edges
- **Space**: O(E)
- Simple but slow for queries

## Common Algorithms

### Traversal
1. **Breadth-First Search (BFS)**
   - Uses Queue
   - Level-by-level exploration
   - Shortest path in unweighted graph
   - Time: O(V + E), Space: O(V)

2. **Depth-First Search (DFS)**
   - Uses Stack/Recursion
   - Explore as far as possible
   - Detecting cycles, topological sort
   - Time: O(V + E), Space: O(V)

### Shortest Path
1. **Dijkstra's Algorithm**
   - Single source shortest path
   - Works with non-negative weights
   - Time: O((V + E) log V)

2. **Bellman-Ford Algorithm**
   - Single source shortest path
   - Works with negative weights
   - Detects negative cycles
   - Time: O(VE)

3. **Floyd-Warshall Algorithm**
   - All pairs shortest path
   - Time: O(V³)

### Minimum Spanning Tree
1. **Kruskal's Algorithm**
   - Sort edges by weight
   - Use Union-Find
   - Time: O(E log E)

2. **Prim's Algorithm**
   - Grow tree from starting vertex
   - Use priority queue
   - Time: O((V + E) log V)

## Applications
- Social Networks (Facebook, LinkedIn)
- Maps and Navigation (Google Maps)
- Network Routing (Internet)
- Recommendation Systems
- Dependency Resolution
- Game Development (pathfinding)

## Files in this directory
- `graph_implementation.py`: Graph representations and basic operations
- `graph_traversal.py`: BFS and DFS implementations
