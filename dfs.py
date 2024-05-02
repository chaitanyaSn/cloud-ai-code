def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize a set to keep track of visited vertices
    visited.add(start)  # Mark the current vertex as visited
    print(start)        # Process the current vertex (in this example, we print it)
    # Recursively visit all unvisited neighboring vertices
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform DFS starting from vertex 'A'
print("DFS traversal:")
dfs(graph, 'A')
