def merge_sort(numbers):
    """Return a new list containing the numbers in sorted order."""
    if len(numbers) <= 1:
        return numbers[:]

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    print(merge_sort([8, 3, 5, 1, 9, 2]))
