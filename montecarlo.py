import random


def estimate_pi(number_of_points=10000):
    """Estimate pi by randomly sampling points in a unit square."""
    if number_of_points <= 0:
        raise ValueError("number_of_points must be positive")
    inside = 0
    for _ in range(number_of_points):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside += 1
    return 4 * inside / number_of_points


if __name__ == "__main__":
    print(estimate_pi())
