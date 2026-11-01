def greedy_vertex_cover(vertices, edges):
    """Greedy 2-approximation: choose both endpoints of each uncovered edge."""
    uncovered_edges = set(tuple(edge) for edge in edges)
    cover = set()

    while uncovered_edges:
        first, second = uncovered_edges.pop()
        cover.add(first)
        cover.add(second)
        uncovered_edges = {
            edge for edge in uncovered_edges
            if first not in edge and second not in edge
        }

    return cover


if __name__ == "__main__":
    nodes = {1, 2, 3, 4}
    links = [(1, 2), (2, 3), (3, 4)]
    print(greedy_vertex_cover(nodes, links))
