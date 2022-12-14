from pathlib import Path

DATA = Path(__file__).parent / "data.txt"


def find_signal_strengths():
    instructions = DATA.read_text().splitlines()

    x: int = 1
    cycle: int = 1
    cycle_strength: int = 20
    signal_strengths: list[int] = []

    def cadd(_cycle: int, _x: int, _strength):
        _cycle += 1
        if _cycle == _strength:
            signal_strengths.append(_x * _strength)
            _strength += 40
        return _x, _cycle, _strength

    for instruction in instructions:
        match instruction.split():
            case ["noop"]:
                x, cycle, cycle_strength = cadd(cycle, x, cycle_strength)
            case ["addx", increment]:
                x, cycle, cycle_strength = cadd(cycle, x, cycle_strength)
                x, cycle, cycle_strength = cadd(cycle, x + int(increment), cycle_strength)
    return sum(signal_strengths)


"""
###  ###  ####  ##  ###   ##  ####  ##  
#  # #  #    # #  # #  # #  #    # #  # 
#  # ###    #  #    #  # #  #   #  #  # 
###  #  #  #   # ## ###  ####  #   #### 
#    #  # #    #  # # #  #  # #    #  # 
#    ###  ####  ### #  # #  # #### #  #
"""


def find_signal_strengths2():
    instructions = DATA.read_text().splitlines()

    x: int = 1
    cycle: int = 0
    length: int = 40
    crts: list[list[str]] = []

    def clear(lst: list[str]):
        for i in range(len(lst)):
            lst[i] = "."

    def update_crt(crt: list[str], _c: int):
        crt[_c] = "#" if current_sprite[_c] == "#" else " "

    def update_sprite(sprite: list[str], _x: int):
        clear(sprite)
        if 39 > _x > 0:
            sprite[_x] = "#"
            sprite[_x-1] = "#"
            sprite[_x+1] = "#"

    current_crt: list[str] = ["." for _ in range(40)]
    current_sprite: list[str] = ["." for _ in range(40)]
    update_sprite(current_sprite, x)

    def reset():
        clear(current_crt)
        clear(current_sprite)
        update_sprite(current_sprite, 1)

    def cadd(_cycle: int, _x: int):
        if _cycle == length:
            _cycle = 0
            crts.append(current_crt.copy())
            reset()
            pass
        update_crt(current_crt, _cycle)
        update_sprite(current_sprite, _x)
        _cycle += 1
        return _x, _cycle

    for instruction in instructions:
        match instruction.split():
            case ["noop"]:
                x, cycle = cadd(cycle, x)
            case ["addx", increment]:
                x, cycle = cadd(cycle, x)
                x, cycle = cadd(cycle, x + int(increment))
    crts.append(current_crt.copy())

    for crt in crts:
        print("".join(crt))


if __name__ == '__main__':
    print(find_signal_strengths())
    print(find_signal_strengths2())