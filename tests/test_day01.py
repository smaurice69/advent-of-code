import sys
from pathlib import Path

# Ensure the project root is on sys.path so "aoc2017" can be imported
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from aoc2017.day01.solution import part1, part2


def test_part1_examples():
    assert part1("1122") == 3
    assert part1("1111") == 4
    assert part1("1234") == 0
    assert part1("91212129") == 9


def test_part2_examples():
    assert part2("1212") == 6
    assert part2("1221") == 0
    assert part2("123425") == 4
    assert part2("123123") == 12
    assert part2("12131415") == 4
