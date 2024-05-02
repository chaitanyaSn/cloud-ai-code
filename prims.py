def prims(graph):
    # Initialize a list to store the MST (Minimum Spanning Tree)
    mst = []
    # Initialize a set to keep track of visited vertices
    visited = set()
    # Start with the first vertex in the graph
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)
    # Initialize total cost of MST
    total_cost = 0

    while len(visited) < len(graph):
        min_edge = None
        min_weight = float('inf')
        # Iterate through visited vertices
        for vertex in visited:
            # Iterate through neighboring vertices of visited vertices
            for neighbor, weight in graph[vertex].items():
                # Check if the neighboring vertex is not visited and the weight is minimum
                if neighbor not in visited and weight < min_weight:
                    min_edge = (vertex, neighbor)
                    min_weight = weight
        
        # Add the minimum weight edge to the MST
        mst.append(min_edge)
        # Add the weight of the added edge to the total cost
        total_cost += min_weight
        # Add the newly visited vertex to the visited set
        visited.add(min_edge[1])

    return mst, total_cost

# Example graph represented as adjacency list
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 3, 'B': 1, 'D': 2},
    'D': {'B': 3, 'C': 2}
}

mst, total_cost = prims(graph)
print("Minimum Spanning Tree (MST):", mst)
print("Total Cost of MST:", total_cost)

