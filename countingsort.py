def counting_sort(numbers):
    """Sort integers, including negative values."""
    if not numbers:
        return []

    smallest = min(numbers)
    largest = max(numbers)
    counts = [0] * (largest - smallest + 1)

    for number in numbers:
        counts[number - smallest] += 1

    result = []
    for index, count in enumerate(counts):
        result.extend([index + smallest] * count)
    return result


if __name__ == "__main__":
    print(counting_sort([4, -2, 2, 8, 3, 3, -2]))
