from pathlib import Path


def find_top_calories() -> int:
    calories = Path("data.txt").read_text().splitlines()

    current_total: int = 0
    elves_calories: set[int] = set()
    for calorie in calories:
        if not calorie:
            elves_calories.add(current_total)
            current_total = 0
            continue
        current_total += int(calorie)
    return max(elves_calories)


def find_topk_calories() -> int:
    calories = Path("data.txt").read_text().splitlines()

    k: int = 3
    current_total: int = 0
    elves_calories: set[int] = set()
    for calorie in calories:
        if not calorie:
            elves_calories.add(current_total)
            current_total = 0
            continue
        current_total += int(calorie)
    topk_calories = sum(sorted(elves_calories)[-k:])
    return topk_calories


print(find_top_calories())
print(find_topk_calories())
