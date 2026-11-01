import heapq
from itertools import count


def build_huffman_codes(frequencies):
    """Return a dictionary mapping each character to its Huffman bit string."""
    if not frequencies:
        return {}
    unique_order = count()
    heap = [(frequency, next(unique_order), character)
            for character, frequency in frequencies.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        character = heap[0][2]
        return {character: "0"}

    while len(heap) > 1:
        frequency_a, _, left = heapq.heappop(heap)
        frequency_b, _, right = heapq.heappop(heap)
        heapq.heappush(heap, (frequency_a + frequency_b, next(unique_order), (left, right)))

    codes = {}
    def assign_codes(node, prefix):
        if isinstance(node, str):
            codes[node] = prefix
            return
        left, right = node
        assign_codes(left, prefix + "0")
        assign_codes(right, prefix + "1")

    assign_codes(heap[0][2], "")
    return codes


if __name__ == "__main__":
    print(build_huffman_codes({"a": 5, "b": 9, "c": 12, "d": 13, "e": 16, "f": 45}))
