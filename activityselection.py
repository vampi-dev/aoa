def activity_selection(activities):
    """Activities are (start, finish) pairs; return a maximum-size compatible set."""
    activities = sorted(activities, key=lambda activity: activity[1])
    selected = []
    last_finish = float("-inf")

    for start, finish in activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    return selected


if __name__ == "__main__":
    tasks = [(1, 3), (2, 5), (4, 7), (1, 8), (8, 9)]
    print(activity_selection(tasks))
