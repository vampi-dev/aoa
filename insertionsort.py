def insertion_sort(numbers):
    numbers = numbers[:]
    for i in range(1, len(numbers)):
        current = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > current:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = current
    return numbers


if __name__ == "__main__":
    print(insertion_sort([9, 5, 1, 4, 3]))
