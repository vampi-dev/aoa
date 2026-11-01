def greedy_set_cover(universe, subsets):
    """Greedy approximation: repeatedly choose the set covering most uncovered items."""
    uncovered = set(universe)
    chosen = []

    while uncovered:
        best_set = max(subsets, key=lambda subset: len(uncovered & set(subset)), default=set())
        newly_covered = uncovered & set(best_set)
        if not newly_covered:
            raise ValueError("The supplied subsets cannot cover the whole universe")
        chosen.append(set(best_set))
        uncovered -= newly_covered

    return chosen


if __name__ == "__main__":
    universe = {1, 2, 3, 4, 5}
    subsets = [{1, 2, 3}, {2, 4}, {3, 4, 5}]
    print(greedy_set_cover(universe, subsets))
