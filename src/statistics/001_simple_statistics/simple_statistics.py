try:
    from src.statistics.common import random_list_generator
except ModuleNotFoundError:
    # When running this file directly, the package root may not be on sys.path.
    # Add the project root (parent of "src") so the "src" package can be imported.
    import sys
    from pathlib import Path

    project_root = Path(__file__).resolve().parents[3]
    sys.path.insert(0, str(project_root))
    from src.statistics.common import random_list_generator


def _sum(x: int, y: int) -> int:
    return x + y


def _list_sum() -> None:
    random_list = random_list_generator.generate_random_list(10, 100)
    print(sum(random_list))
    return None


def main():
    result = _sum(1, 2)
    print("simple sum : $", result)
    _list_sum()


if __name__ == "__main__":
    main()
