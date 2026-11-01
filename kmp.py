def build_lps(pattern):
    """Build the longest-prefix-suffix table used by KMP."""
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]
        else:
            i += 1
    return lps


def kmp_search(text, pattern):
    if pattern == "":
        return list(range(len(text) + 1))
    lps = build_lps(pattern)
    positions = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                positions.append(i - j)
                j = lps[j - 1]
        elif j:
            j = lps[j - 1]
        else:
            i += 1
    return positions


if __name__ == "__main__":
    print(kmp_search("ABABDABACDABABCABAB", "ABAB"))
