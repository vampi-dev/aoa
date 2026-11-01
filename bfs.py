from collections import deque


def bfs(graph, start):
    visited = set()
    order = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex in visited:
            continue
        visited.add(vertex)
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                queue.append(neighbor)
    return order


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
    print(bfs(graph, "A"))
