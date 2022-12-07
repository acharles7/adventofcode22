from pathlib import Path

DATA = Path(__file__).parent / "data.txt"


#     [C]         [Q]         [V]
#     [D]         [D] [S]     [M] [Z]
#     [G]     [P] [W] [M]     [C] [G]
#     [F]     [Z] [C] [D] [P] [S] [W]
# [P] [L]     [C] [V] [W] [W] [H] [L]
# [G] [B] [V] [R] [L] [N] [G] [P] [F]
# [R] [T] [S] [S] [S] [T] [D] [L] [P]
# [N] [J] [M] [L] [P] [C] [H] [Z] [R]
#  1   2   3   4   5   6   7   8   9

CRATES = {
    1: ["N", "R", "G", "P"],
    2: ["J", "T", "B", "L", "F", "G", "D", "C"],
    3: ["M", "S", "V"],
    4: ["L", "S", "R", "C", "Z", "P"],
    5: ["P", "S", "L", "V", "C", "W", "D", "Q"],
    6: ["C", "T", "N", "W", "D", "M", "S"],
    7: ["H", "D", "G", "W", "P"],
    8: ["Z", "L", "P", "H", "S", "C", "M", "V"],
    9: ["R", "P", "F", "L", "W", "G", "Z"],
}


def find_rearrangements() -> str:
    procedures = DATA.read_text().splitlines()

    for procedure in procedures:
        _, n, _, f, _, t = procedure.split()
        from_stack, to_stack = CRATES[int(f)], CRATES[int(t)]

        for i in range(int(n)):
            to_stack.append(from_stack.pop())
    return "".join(crates[-1] for _, crates in CRATES.items())


def find_rearrangements2() -> str:
    procedures = DATA.read_text().splitlines()

    for procedure in procedures:
        _, n, _, f, _, t = procedure.split()
        from_stack, to_stack = CRATES[int(f)], CRATES[int(t)]

        to_stack += from_stack[-int(n):]
        del from_stack[-int(n):]
    return "".join(crates[-1] for _, crates in CRATES.items())


if __name__ == '__main__':
    print(find_rearrangements())
    print(find_rearrangements2())
