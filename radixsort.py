def radix_sort(numbers):
    """Sort non-negative integers using base-10 digit positions."""
    if any(number < 0 for number in numbers):
        raise ValueError("Radix sort in this example accepts non-negative integers only.")
    numbers = numbers[:]
    if not numbers:
        return numbers

    place = 1
    largest = max(numbers)
    while largest // place > 0:
        buckets = [[] for _ in range(10)]
        for number in numbers:
            digit = (number // place) % 10
            buckets[digit].append(number)
        numbers = [number for bucket in buckets for number in bucket]
        place *= 10
    return numbers


if __name__ == "__main__":
    print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
