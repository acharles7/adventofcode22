from pathlib import Path

DATA = Path(__file__).parent / "data.txt"


def find_visited():
    motions = DATA.read_text().splitlines()
    h_moves = map(lambda m: (m[0], int(m[1])), map(str.split, motions))

    visited = set()
    head, tail = [0, 0], [0, 0]

    def adjacent(h: list[int], t: list[int]) -> bool:
        neighbours = [
            [h[0], h[1]],      # overlap
            [h[0], h[1]-1],    # left
            [h[0], h[1]+1],    # right
            [h[0]-1, h[1]],    # top
            [h[0]+1, h[1]],    # bottom
            [h[0]-1, h[1]-1],  # top-left
            [h[0]-1, h[1]+1],  # top-right
            [h[0]+1, h[1]-1],  # bottom-left
            [h[0]+1, h[1]+1]   # bottom-right
        ]
        return t in neighbours

    for direction, steps in h_moves:
        for step in range(steps):
            match direction:
                case "R":
                    head = [head[0], head[1] + 1]
                case "L":
                    head = [head[0], head[1] - 1]
                case "U":
                    head = [head[0] - 1, head[1]]
                case "D":
                    head = [head[0] + 1, head[1]]
            if not adjacent(head, tail):
                match direction:
                    case "R":
                        tail = [head[0], tail[1] + 1]
                    case "L":
                        tail = [head[0], tail[1] - 1]
                    case "U":
                        tail = [tail[0] - 1, head[1]]
                    case "D":
                        tail = [tail[0] + 1, head[1]]
                visited.add(tuple(tail))
    return len(visited)


if __name__ == '__main__':
    print(find_visited())
