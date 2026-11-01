def naive_search(text, pattern):
    """Return all starting positions where pattern occurs in text."""
    if pattern == "":
        return list(range(len(text) + 1))
    positions = []
    for start in range(len(text) - len(pattern) + 1):
        if text[start:start + len(pattern)] == pattern:
            positions.append(start)
    return positions


if __name__ == "__main__":
    print(naive_search("ABABDABACDABABCABAB", "ABAB"))
