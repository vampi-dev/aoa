def boyer_moore_search(text, pattern):
    """Boyer-Moore search using the bad-character rule."""
    if pattern == "":
        return list(range(len(text) + 1))

    last_position = {character: index for index, character in enumerate(pattern)}
    positions = []
    shift = 0
    while shift <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            positions.append(shift)
            next_character = text[shift + len(pattern)] if shift + len(pattern) < len(text) else None
            shift += len(pattern) - last_position.get(next_character, -1) if next_character is not None else 1
        else:
            shift += max(1, j - last_position.get(text[shift + j], -1))
    return positions


if __name__ == "__main__":
    print(boyer_moore_search("HERE IS A SIMPLE EXAMPLE", "EXAMPLE"))
