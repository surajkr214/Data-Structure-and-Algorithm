"""
Graph Implementation
Demonstrates graph data structure using adjacency list representation.
"""

from collections import deque, defaultdict


class Graph:
    """Graph implementation using adjacency list."""
    
    def __init__(self, directed=False):
        """
        Initialize a graph.
        
        Args:
            directed: If True, creates a directed graph; otherwise undirected
        """
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        Time Complexity: O(1)
        """
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, u, v, weight=1):
        """
        Add an edge between vertices u and v.
        
        Args:
            u: Source vertex
            v: Destination vertex
            weight: Weight of the edge (default 1)
        
        Time Complexity: O(1)
        """
        # Add edge from u to v
        self.graph[u].append((v, weight))
        
        # If undirected, add edge from v to u
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def remove_edge(self, u, v):
        """
        Remove an edge between vertices u and v.
        Time Complexity: O(E) where E is number of edges from u
        """
        self.graph[u] = [(vertex, weight) for vertex, weight in self.graph[u] if vertex != v]
        
        if not self.directed:
            self.graph[v] = [(vertex, weight) for vertex, weight in self.graph[v] if vertex != u]
    
    def remove_vertex(self, vertex):
        """
        Remove a vertex and all its edges.
        Time Complexity: O(V + E)
        """
        if vertex in self.graph:
            # Remove all edges to this vertex
            for v in self.graph:
                self.graph[v] = [(u, w) for u, w in self.graph[v] if u != vertex]
            
            # Remove the vertex itself
            del self.graph[vertex]
    
    def get_neighbors(self, vertex):
        """
        Get all neighbors of a vertex.
        Time Complexity: O(1)
        """
        return [v for v, w in self.graph.get(vertex, [])]
    
    def get_vertices(self):
        """Get all vertices in the graph."""
        return list(self.graph.keys())
    
    def get_edges(self):
        """Get all edges in the graph."""
        edges = []
        for u in self.graph:
            for v, weight in self.graph[u]:
                if self.directed or u <= v:  # Avoid duplicates for undirected
                    edges.append((u, v, weight))
        return edges
    
    def bfs(self, start):
        """
        Breadth-First Search traversal.
        
        Args:
            start: Starting vertex
        
        Returns:
            List of vertices in BFS order
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = set()
        queue = deque([start])
        result = []
        
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """
        Depth-First Search traversal (iterative).
        
        Args:
            start: Starting vertex
        
        Returns:
            List of vertices in DFS order
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Add neighbors in reverse order to maintain left-to-right order
                for neighbor, _ in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def dfs_recursive(self, start, visited=None):
        """
        Depth-First Search traversal (recursive).
        
        Args:
            start: Starting vertex
            visited: Set of visited vertices
        
        Returns:
            List of vertices in DFS order
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        if visited is None:
            visited = set()
        
        result = []
        
        if start not in visited:
            visited.add(start)
            result.append(start)
            
            for neighbor, _ in self.graph[start]:
                if neighbor not in visited:
                    result.extend(self.dfs_recursive(neighbor, visited))
        
        return result
    
    def has_cycle(self):
        """
        Detect if graph has a cycle.
        Works for both directed and undirected graphs.
        
        Returns:
            True if cycle exists, False otherwise
        
        Time Complexity: O(V + E)
        """
        visited = set()
        
        def dfs_cycle(vertex, parent):
            visited.add(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs_cycle(neighbor, vertex):
                        return True
                else:
                    # For directed graphs, any visited neighbor is a back edge (cycle)
                    # For undirected graphs, only if neighbor is not parent
                    if self.directed or neighbor != parent:
                        return True
            
            return False
        
        for vertex in self.graph:
            if vertex not in visited:
                if dfs_cycle(vertex, None):
                    return True
        
        return False
    
    def shortest_path_bfs(self, start, end):
        """
        Find shortest path between two vertices using BFS.
        Works for unweighted graphs.
        
        Args:
            start: Starting vertex
            end: Ending vertex
        
        Returns:
            List representing shortest path, or None if no path exists
        
        Time Complexity: O(V + E)
        """
        if start == end:
            return [start]
        
        visited = {start}
        queue = deque([(start, [start])])
        
        while queue:
            vertex, path = queue.popleft()
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor == end:
                    return path + [neighbor]
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None  # No path found
    
    def display(self):
        """Display the graph."""
        print(f"Graph ({'Directed' if self.directed else 'Undirected'}):")
        for vertex in sorted(self.graph.keys()):
            neighbors = [f"{v}({w})" for v, w in self.graph[vertex]]
            print(f"  {vertex} -> {', '.join(neighbors)}")


# Example usage
if __name__ == "__main__":
    # Create an undirected graph
    print("=== Undirected Graph ===")
    g = Graph(directed=False)
    
    # Add edges
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
    for u, v in edges:
        g.add_edge(u, v)
    
    g.display()
    
    # BFS traversal
    print(f"\nBFS from vertex 0: {g.bfs(0)}")
    
    # DFS traversal
    print(f"DFS from vertex 0: {g.dfs(0)}")
    print(f"DFS Recursive from vertex 0: {g.dfs_recursive(0)}")
    
    # Shortest path
    path = g.shortest_path_bfs(0, 4)
    print(f"\nShortest path from 0 to 4: {path}")
    
    # Cycle detection
    print(f"Has cycle: {g.has_cycle()}")
    
    # Create a directed graph
    print("\n=== Directed Graph ===")
    dg = Graph(directed=True)
    
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    for u, v in edges:
        dg.add_edge(u, v)
    
    dg.display()
    
    print(f"\nBFS from vertex A: {dg.bfs('A')}")
    print(f"DFS from vertex A: {dg.dfs('A')}")
    
    # Neighbors
    print(f"\nNeighbors of A: {dg.get_neighbors('A')}")
    
    # All edges
    print(f"All edges: {dg.get_edges()}")
