def subset_sum(numbers, target):
    """Return one subset adding to target, or None if no subset is found."""
    possible = {0: []}
    for number in numbers:
        new_possible = dict(possible)
        for current_sum, chosen in possible.items():
            next_sum = current_sum + number
            if next_sum not in new_possible:
                new_possible[next_sum] = chosen + [number]
        possible = new_possible
    return possible.get(target)


if __name__ == "__main__":
    print(subset_sum([3, 4, 5, 2], 9))
