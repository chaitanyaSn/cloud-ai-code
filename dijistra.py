def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Set to keep track of visited nodes
    visited = set()
    
    while len(visited) < len(graph):
        # Find the node with the shortest distance among unvisited nodes
        min_node = None
        min_distance = float('inf')
        for node, distance in distances.items():
            if node not in visited and distance < min_distance:
                min_node = node
                min_distance = distance
        
        # Mark the node as visited
        visited.add(min_node)
        
        # Update distances for neighbors of the current node
        for neighbor, weight in graph[min_node].items():
            if neighbor not in visited:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    return distances

# Example graph represented as adjacency list
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 3, 'B': 1, 'D': 2},
    'D': {'B': 3, 'C': 2}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node, "to")
for node, distance in distances.items():
    print("Node:", node, "Distance:", distance)

