def k_largest(numbers, k):
    if k < 0 or k > len(numbers):
        raise ValueError("k must be between 0 and the list length")
    return sorted(numbers, reverse=True)[:k]


if __name__ == "__main__":
    print(k_largest([4, 1, 9, 7, 2, 8], 3))
