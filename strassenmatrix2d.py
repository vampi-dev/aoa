def add_matrix(a, b):
    size = len(a)
    return [[a[i][j] + b[i][j] for j in range(size)] for i in range(size)]


def subtract_matrix(a, b):
    size = len(a)
    return [[a[i][j] - b[i][j] for j in range(size)] for i in range(size)]


def strassen(a, b):
    """Multiply equally sized square matrices; size must be a power of two."""
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]
    if n == 0 or n & (n - 1):
        raise ValueError("Matrix size must be a positive power of two.")
    if any(len(row) != n for row in a + b):
        raise ValueError("Matrices must be square and have the same size.")

    half = n // 2
    a11 = [row[:half] for row in a[:half]]
    a12 = [row[half:] for row in a[:half]]
    a21 = [row[:half] for row in a[half:]]
    a22 = [row[half:] for row in a[half:]]
    b11 = [row[:half] for row in b[:half]]
    b12 = [row[half:] for row in b[:half]]
    b21 = [row[:half] for row in b[half:]]
    b22 = [row[half:] for row in b[half:]]

    m1 = strassen(add_matrix(a11, a22), add_matrix(b11, b22))
    m2 = strassen(add_matrix(a21, a22), b11)
    m3 = strassen(a11, subtract_matrix(b12, b22))
    m4 = strassen(a22, subtract_matrix(b21, b11))
    m5 = strassen(add_matrix(a11, a12), b22)
    m6 = strassen(subtract_matrix(a21, a11), add_matrix(b11, b12))
    m7 = strassen(subtract_matrix(a12, a22), add_matrix(b21, b22))

    c11 = add_matrix(subtract_matrix(add_matrix(m1, m4), m5), m7)
    c12 = add_matrix(m3, m5)
    c21 = add_matrix(m2, m4)
    c22 = add_matrix(subtract_matrix(add_matrix(m1, m3), m2), m6)

    top = [c11[i] + c12[i] for i in range(half)]
    bottom = [c21[i] + c22[i] for i in range(half)]
    return top + bottom


if __name__ == "__main__":
    print(strassen([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
