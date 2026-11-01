def prims_algorithm(graph, start):
    """Return the edges of a minimum spanning tree for a connected graph.
    graph[u] contains (neighbor, weight) pairs.
    """
    visited = {start}
    tree_edges = []

    while len(visited) < len(graph):
        best_edge = None
        for vertex in visited:
            for neighbor, weight in graph[vertex]:
                if neighbor not in visited:
                    if best_edge is None or weight < best_edge[2]:
                        best_edge = (vertex, neighbor, weight)
        if best_edge is None:
            raise ValueError("The graph is not connected")
        tree_edges.append(best_edge)
        visited.add(best_edge[1])

    return tree_edges


if __name__ == "__main__":
    graph = {
        "A": [("B", 2), ("C", 3)],
        "B": [("A", 2), ("C", 1), ("D", 4)],
        "C": [("A", 3), ("B", 1), ("D", 5)],
        "D": [("B", 4), ("C", 5)]
    }
    print(prims_algorithm(graph, "A"))
