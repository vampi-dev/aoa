def optimal_bst_cost(frequencies):
    """Return minimum search cost for ordered keys with successful frequencies.
    This simplified version assumes only successful searches.
    """
    n = len(frequencies)
    cost = [[0] * n for _ in range(n)]
    prefix = [0]
    for frequency in frequencies:
        prefix.append(prefix[-1] + frequency)

    for length in range(1, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            total = prefix[end + 1] - prefix[start]
            best = float("inf")
            for root in range(start, end + 1):
                left = cost[start][root - 1] if root > start else 0
                right = cost[root + 1][end] if root < end else 0
                best = min(best, left + right + total)
            cost[start][end] = best

    return cost[0][n - 1] if n else 0


if __name__ == "__main__":
    print(optimal_bst_cost([34, 8, 50]))
