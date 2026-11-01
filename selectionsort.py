def selection_sort(numbers):
    numbers = numbers[:]
    for i in range(len(numbers)):
        smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[smallest]:
                smallest = j
        numbers[i], numbers[smallest] = numbers[smallest], numbers[i]
    return numbers


if __name__ == "__main__":
    print(selection_sort([64, 25, 12, 22, 11]))
