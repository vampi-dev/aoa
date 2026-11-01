def quick_sort(numbers):
    """Return a sorted copy using the last item as the pivot."""
    if len(numbers) <= 1:
        return numbers[:]

    pivot = numbers[-1]
    smaller = [item for item in numbers[:-1] if item <= pivot]
    larger = [item for item in numbers[:-1] if item > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(larger)


if __name__ == "__main__":
    print(quick_sort([7, 2, 9, 1, 5, 2]))
