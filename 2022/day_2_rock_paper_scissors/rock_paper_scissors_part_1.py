from enum import Enum

class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def read_file(path):
    return open(path).read()

def format_input(input):
    return [[convert(shape) for shape in round.split(' ')] for round in input.splitlines()]

def convert(shape):
    if shape == 'A' or shape == 'X': return 1
    if shape == 'B' or shape == 'Y': return 2
    if shape == 'C' or shape == 'Z': return 3

def decrypt_strategy_guide(path):
    file = read_file(path)
    rounds = format_input(file)
    score = 0
    for round in rounds:
        opponent, player = round
        if won(player, opponent):
            score += 6
        elif draw(player, opponent):
            score += 3
        score += player
    return score

def won(player, opponent):
    return ((player == Shape.ROCK.value and opponent == Shape.SCISSORS.value) or 
        (player == Shape.PAPER.value and opponent == Shape.ROCK.value) or
        (player == Shape.SCISSORS.value and opponent == Shape.PAPER.value))

def draw(player, opponent):
    return player == opponent

path = '2022/day_2_rock_paper_scissors/encrypted_strategy_guide.txt'
print(decrypt_strategy_guide(path))