from pathlib import Path

DATA = Path(__file__).parent / "data.txt"


def find_visible_trees() -> int:
    trees = DATA.read_text().splitlines()

    forest = [list(map(int, list(tree))) for tree in trees]
    row, col = len(forest), len(forest[0])
    inner_trees: int = 0
    edge_trees: int = (row + col) * 2 - 4

    def is_visible(height: int, i: int, j: int) -> bool:
        _row = forest[i]
        _col = [forest[r][c] for r in range(row) for c in range(col) if c == j]

        r_right, r_left = _row[:j], _row[j + 1:]
        c_bottom, c_top = _col[i + 1:], _col[:i]

        r_r = [x for x in r_right if x >= height]
        l_r = [x for x in r_left if x >= height]
        t_c = [x for x in c_top if x >= height]
        b_c = [x for x in c_bottom if x >= height]

        return any([not r_r, not l_r, not t_c, not b_c])

    for r in range(row):
        if r == 0 or r == row - 1:
            continue
        for c in range(col):
            if c == 0 or c == col - 1:
                continue
            inner_trees += is_visible(forest[r][c], r, c)

    return inner_trees + edge_trees


def find_max_scenic_score() -> int:
    trees = DATA.read_text().splitlines()

    forest = [list(map(int, list(tree))) for tree in trees]
    row, col = len(forest), len(forest[0])
    scenic_scores: list[int] = []

    def find_count(ts: list, height: int):
        tc = 0
        for t in ts:
            if t >= height:
                tc += 1
                return tc
            tc += 1
        return tc

    def find_score(height: int, i: int, j: int) -> int:
        _row = forest[i]
        _col = [forest[r][c] for r in range(row) for c in range(col) if c == j]

        r_right, r_left = _row[:j], _row[j + 1:]
        c_bottom, c_top = _col[i + 1:], _col[:i]

        r_r = find_count(list(reversed(r_right)), height)
        l_r = find_count(r_left, height)
        t_c = find_count(list(reversed(c_top)), height)
        b_c = find_count(c_bottom, height)

        return r_r * l_r * t_c * b_c

    for r in range(row):
        if r == 0 or r == row - 1:
            continue
        for c in range(col):
            if c == 0 or c == col - 1:
                continue
            scenic_scores.append(find_score(forest[r][c], r, c))
    return max(scenic_scores)


if __name__ == '__main__':
    print(find_visible_trees())
    print(find_max_scenic_score())
