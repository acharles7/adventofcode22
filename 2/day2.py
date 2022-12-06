from pathlib import Path
from enum import Enum


DATA = Path(__file__).parent / "data.txt"


class Shape(Enum):

    ROCK = 1
    PAPER = 2
    SCISSOR = 3


class Result(Enum):

    WON = 6
    DRAW = 3
    LOST = 0


class Opponent(Enum):

    ROCK = "A"
    PAPER = "B"
    SCISSOR = "C"


class Player(Enum):

    ROCK = "X"
    PAPER = "Y"
    SCISSOR = "Z"


SCORING = {shape.name: shape.value for shape in Shape}

RULES = {
    (Shape.ROCK, Shape.SCISSOR): Result.LOST,
    (Shape.SCISSOR, Shape.ROCK): Result.WON,
    (Shape.SCISSOR, Shape.PAPER): Result.LOST,
    (Shape.PAPER, Shape.SCISSOR): Result.WON,
    (Shape.ROCK, Shape.PAPER): Result.WON,
    (Shape.PAPER, Shape.ROCK): Result.LOST,

    (Shape.PAPER, Shape.PAPER): Result.DRAW,
    (Shape.ROCK, Shape.ROCK): Result.DRAW,
    (Shape.SCISSOR, Shape.SCISSOR): Result.DRAW,
}

STRATEGY = {"X": Result.LOST, "Y": Result.DRAW, "Z": Result.WON}


def find_score() -> int:
    games = DATA.read_text().splitlines()

    score: int = 0
    for game in games:
        o, p = game.split()
        opponent, player = Opponent(o), Player(p)
        os, ps = SCORING[opponent.name], SCORING[player.name]
        result = RULES[(Shape(os), Shape(ps))]
        score += ps + result.value
    return score


def find_score2() -> int:
    games = DATA.read_text().splitlines()

    score: int = 0
    for game in games:
        _o, _p = game.split()
        opponent, player = Opponent(_o), Player(_p)
        os, ps = SCORING[opponent.name], SCORING[player.name]
        final_result: Result = STRATEGY[_p]
        final_player_shape: Shape

        for (o, p), result in RULES.items():
            if final_result is result and o is Shape(os):
                final_player_shape = p
                break
        score += final_player_shape.value + final_result.value

    return score


if __name__ == '__main__':
    print(find_score())
    print(find_score2())


