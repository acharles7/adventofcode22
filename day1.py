from pathlib import Path


def find_top_calories():
    calories = Path("data.txt").read_text().splitlines()
    elves_calories = set()
    current_total = 0
    for calorie in calories:
        if not calorie:
            elves_calories.add(current_total)
            current_total = 0
            continue
        current_total += int(calorie)
    return max(elves_calories)


def find_topk_calories():
    calories = Path("data.txt").read_text().splitlines()
    elves_calories = set()
    k = 3
    current_total = 0
    for calorie in calories:
        if not calorie:
            elves_calories.add(current_total)
            current_total = 0
            continue
        current_total += int(calorie)
    topk_calories = sum(sorted(elves_calories)[-k:])
    print(topk_calories)


print(find_top_calories())
print(find_topk_calories())
