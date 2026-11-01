import random


def kth_smallest(numbers, k):
    """Return the k-th smallest value (k starts at 1)."""
    if k < 1 or k > len(numbers):
        raise ValueError("k must be between 1 and the number of items")

    items = numbers[:]
    target = k - 1
    left, right = 0, len(items) - 1

    while left <= right:
        pivot_index = random.randint(left, right)
        items[pivot_index], items[right] = items[right], items[pivot_index]
        pivot = items[right]

        smaller_end = left
        for i in range(left, right):
            if items[i] <= pivot:
                items[smaller_end], items[i] = items[i], items[smaller_end]
                smaller_end += 1
        items[smaller_end], items[right] = items[right], items[smaller_end]

        if smaller_end == target:
            return items[smaller_end]
        if smaller_end < target:
            left = smaller_end + 1
        else:
            right = smaller_end - 1


if __name__ == "__main__":
    print(kth_smallest([7, 2, 9, 1, 5], 3))
