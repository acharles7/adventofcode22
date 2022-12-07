from pathlib import Path
from string import ascii_letters

DATA = Path(__file__).parent / "data.txt"

PRIORITIES = {char: priority for priority, char in enumerate(ascii_letters, start=1)}


def find_priorities() -> int:
    rucksacks = DATA.read_text().splitlines()
    priorities: int = 0

    for rucksack in rucksacks:
        n = len(rucksack) // 2
        first_comp, second_comp = rucksack[:n], rucksack[n:]
        common_item = set.intersection(set(first_comp), set(second_comp)).pop()
        priorities += PRIORITIES[common_item]
    return priorities


def find_priorities2() -> int:
    rucksacks = DATA.read_text().splitlines()
    priorities: int = 0

    for group in range(0, len(rucksacks)-1, 3):
        common_item = set.intersection(set(rucksacks[group]), set(rucksacks[group+1]), set(rucksacks[group+2])).pop()
        priorities += PRIORITIES[common_item]
    return priorities


if __name__ == '__main__':
    print(find_priorities())
    print(find_priorities2())


