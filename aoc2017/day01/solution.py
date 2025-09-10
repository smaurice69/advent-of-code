from pathlib import Path


def clean(s: str) -> str:
    """Strip whitespace and remove internal spaces."""
    return s.strip().replace(" ", "")


def part1(data: str) -> int:
    """Return the captcha sum where each digit is compared to the next one."""
    s = clean(data)
    n = len(s)
    total = 0
    for i, ch in enumerate(s):
        if ch == s[(i + 1) % n]:
            total += int(ch)
    return total


def part2(data: str) -> int:
    """Return the captcha sum where each digit is compared to the one halfway around."""
    s = clean(data)
    n = len(s)
    step = n // 2
    total = 0
    for i, ch in enumerate(s):
        if ch == s[(i + step) % n]:
            total += int(ch)
    return total


def main(part: int = 1, path: str | None = None) -> int:
    file_path = Path(path) if path else Path(__file__).with_name("input.txt")
    data = file_path.read_text()
    solver = part1 if part == 1 else part2
    result = solver(data)
    print(result)
    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Solve AoC 2017 Day 1")
    parser.add_argument("--part", type=int, default=1, choices=[1, 2], help="Part to solve")
    parser.add_argument("--file", type=str, help="Input file path", default=None)
    args = parser.parse_args()
    main(args.part, args.file)
