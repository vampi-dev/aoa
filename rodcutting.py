def rod_cutting(prices, rod_length):
    """prices[i - 1] is the price for a piece of length i."""
    best = [0] * (rod_length + 1)
    for length in range(1, rod_length + 1):
        for first_piece in range(1, min(length, len(prices)) + 1):
            best[length] = max(best[length], prices[first_piece - 1] + best[length - first_piece])
    return best[rod_length]


if __name__ == "__main__":
    print(rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 8))
