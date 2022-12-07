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
        assert len(first_comp) == len(second_comp)

        first_comp_items = set(first_comp)
        second_comp_items = set(second_comp)
        common_item = set.intersection(first_comp_items, second_comp_items).pop()
        priorities += PRIORITIES[common_item]
    return priorities


def find_priorities2() -> int:
    rucksacks = DATA.read_text().splitlines()
    priorities: int = 0

    for group in range(-1, len(rucksacks)-2, 3):
        first_elf = set(rucksacks[group+1])
        second_elf = set(rucksacks[group+2])
        third_elf = set(rucksacks[group+3])

        common_item = set.intersection(first_elf, second_elf, third_elf).pop()
        priorities += PRIORITIES[common_item]
    return priorities


if __name__ == '__main__':
    print(find_priorities())
    print(find_priorities2())


