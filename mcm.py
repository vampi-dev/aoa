def matrix_chain_order(dimensions):
    """Return minimum multiplication cost for matrices with given dimensions.
    For matrices A1..An, dimensions is [p0, p1, ..., pn].
    """
    n = len(dimensions) - 1
    if n <= 0:
        return 0
    cost = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            cost[start][end] = float("inf")
            for split in range(start, end):
                current = (cost[start][split] + cost[split + 1][end]
                           + dimensions[start] * dimensions[split + 1] * dimensions[end + 1])
                cost[start][end] = min(cost[start][end], current)
    return cost[0][n - 1]


if __name__ == "__main__":
    print(matrix_chain_order([40, 20, 30, 10, 30]))
