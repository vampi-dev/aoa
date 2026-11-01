def kruskals_algorithm(vertices, edges):
    """Edges are (weight, start, end). Returns minimum spanning tree edges."""
    parent = {vertex: vertex for vertex in vertices}
    rank = {vertex: 0 for vertex in vertices}

    def find(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    def union(first, second):
        root_a = find(first)
        root_b = find(second)
        if root_a == root_b:
            return False
        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_b] = root_a
            rank[root_a] += 1
        return True

    result = []
    for weight, start, end in sorted(edges):
        if union(start, end):
            result.append((start, end, weight))
    if len(result) != max(0, len(vertices) - 1):
        raise ValueError("The graph is not connected")
    return result


if __name__ == "__main__":
    nodes = ["A", "B", "C", "D"]
    edges = [(2, "A", "B"), (3, "A", "C"), (1, "B", "C"), (4, "B", "D"), (5, "C", "D")]
    print(kruskals_algorithm(nodes, edges))
