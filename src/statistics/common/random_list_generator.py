import random


def generate_random_list(size: int, max_value: int) -> list[int]:
    return [
        random.randint(0, max_value)
        for _ in range(size)
    ]
