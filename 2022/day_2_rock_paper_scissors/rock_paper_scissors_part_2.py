from enum import Enum

class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Condition(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

def read_file(path):
    return open(path).read()

def format_input(input):
    return [[convert(symbol) for symbol in round.split(' ')] for round in input.splitlines()]

def convert(symbol):
    if symbol == 'A': return Shape.ROCK
    if symbol == 'B': return Shape.PAPER
    if symbol == 'C': return Shape.SCISSORS
    if symbol == 'X': return Condition.LOSE
    if symbol == 'Y': return Condition.DRAW
    if symbol == 'Z': return Condition.WIN

def decrypt_strategy_guide(path):
    file = read_file(path)
    rounds = format_input(file)

    score = 0
    for round in rounds:
        opponent, condition = round
        if(condition == Condition.WIN):
            score += win(opponent).value
        elif(condition == Condition.LOSE):
            score += lose(opponent).value
        else:
            score += opponent.value
        score += condition.value
    return score

def win(opponent):
    match opponent:
        case Shape.ROCK: return Shape.PAPER
        case Shape.PAPER: return Shape.SCISSORS
        case Shape.SCISSORS: return Shape.ROCK

def lose(opponent):
    match opponent:
        case Shape.ROCK: return Shape.SCISSORS
        case Shape.PAPER: return Shape.ROCK
        case Shape.SCISSORS: return Shape.PAPER

path = '2022/day_2_rock_paper_scissors/encrypted_strategy_guide.txt'
print(decrypt_strategy_guide(path))