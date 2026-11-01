def hire_best_candidate(candidates):
    """Hire a candidate whenever their score beats every earlier score."""
    hired = []
    best_score = float("-inf")
    for name, score in candidates:
        if score > best_score:
            hired.append((name, score))
            best_score = score
    return hired


if __name__ == "__main__":
    people = [("A", 60), ("B", 75), ("C", 70), ("D", 90)]
    print(hire_best_candidate(people))
