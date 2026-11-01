def multiply_2d(a, b):
    """Multiply two square 2D matrices using the ordinary method."""
    n = len(a)
    if n == 0 or any(len(row) != n for row in a + b) or len(b) != n:
        raise ValueError("Each matrix must be square and have the same size.")
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def multiply_matrix_batches(batch_a, batch_b):
    """Multiply corresponding 2D matrices in two equally sized batches."""
    if len(batch_a) != len(batch_b):
        raise ValueError("Both batches must contain the same number of matrices.")
    return [multiply_2d(a, b) for a, b in zip(batch_a, batch_b)]


if __name__ == "__main__":
    first = [[[1, 2], [3, 4]], [[2, 0], [1, 2]]]
    second = [[[5, 6], [7, 8]], [[1, 3], [2, 1]]]
    print(multiply_matrix_batches(first, second))
