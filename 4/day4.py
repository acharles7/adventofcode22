from pathlib import Path

DATA = Path(__file__).parent / "data.txt"


def find_overlaps() -> int:
    sections = DATA.read_text().splitlines()

    overlaps: int = 0
    for section in sections:
        first, second = section.split(",")
        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")
        overlap: bool = False

        if int(second_start) <= int(first_start) and int(second_end) >= int(first_end):
            overlap = True

        if int(first_start) <= int(second_start) and int(first_end) >= int(second_end):
            overlap = True

        overlaps += overlap
    return overlaps


def find_overlaps2() -> int:
    sections = DATA.read_text().splitlines()

    overlaps: int = 0
    for section in sections:
        first, second = section.split(",")
        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")
        overlaps += not (int(second_start) > int(first_end) or int(second_end) < int(first_start))
    return overlaps


if __name__ == '__main__':
    print(find_overlaps())
    print(find_overlaps2())
