def dfs(graph, start):
    visited = set()
    order = []

    def visit(vertex):
        if vertex in visited:
            return
        visited.add(vertex)
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            visit(neighbor)

    visit(start)
    return order


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
    print(dfs(graph, "A"))
