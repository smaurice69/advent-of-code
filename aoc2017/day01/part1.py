import enum

def solve_captcha(s: str) -> int:
    """
    Sum digits that match the next digit in the circular list.
    s: input string of digits (e.g., "1122")
    """
   # s = s.strip()
    s = clean(s)
    n = len(s)
    if n == 0:
        return 0

    total = 0
    for i, ch in enumerate(s):
        if ch == s[(i + 1) % n]:
            total += int(ch)
    return total

def solve_captcha2(s: str) -> int:
    s = clean(s)
    n = len(s)
    if n == 0:
        return 0
    total = 0
    for i, ch in enumerate(s):
        if ch == s[(i + int(n/2)) % n]:
            total += int(ch)


    return total


def solve_file(path: str = __file__.replace("part1.py", "input.txt")) -> int:
    with open(path, "r", encoding="utf-8") as f:
        data = f.read().strip()
    return solve_captcha(data)

def solve_file2(path: str = __file__.replace("part1.py", "input.txt")) -> int:
    with open(path, "r", encoding="utf-8") as f:
        data = f.read().strip()
    return solve_captcha2(data)


def clean(s: str) -> str:
    """Strip whitespace at both ends and remove inner spaces."""
    # TODO: return s with .strip() and remove spaces
    result = s.replace(' ','')
    return result

    


if __name__ == "__main__":
    print(solve_file())
    print(solve_file2())
