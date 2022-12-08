from pathlib import Path

DATA = Path(__file__).parent / "data.txt"


def find_marker(k: int) -> int:
    datastream: str = DATA.read_text()
    for marker in range(0, len(datastream)-k+1):
        if len(set(datastream[marker:marker+k])) == k:
            return marker+k


if __name__ == '__main__':
    print(find_marker(k=4))
    print(find_marker(k=14))
