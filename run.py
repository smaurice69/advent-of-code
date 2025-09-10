"""Command-line runner for Advent of Code solutions."""
import argparse
import importlib
from pathlib import Path


def run(day: int, part: int, year: int = 2017, file: Path | None = None) -> int:
    module = importlib.import_module(f"aoc{year}.day{day:02d}.solution")
    input_path = file or Path(module.__file__).with_name("input.txt")
    data = input_path.read_text()
    solver = getattr(module, f"part{part}")
    return solver(data)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run an Advent of Code solution")
    parser.add_argument("day", type=int, help="Day to run")
    parser.add_argument("part", type=int, choices=[1, 2], help="Part to run")
    parser.add_argument("--year", type=int, default=2017, help="Event year")
    parser.add_argument("--file", type=Path, help="Override input file", default=None)
    args = parser.parse_args()
    result = run(args.day, args.part, args.year, args.file)
    print(result)


if __name__ == "__main__":
    main()
