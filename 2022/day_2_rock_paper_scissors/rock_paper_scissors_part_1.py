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
    if shape == 'A' or shape == 'X': return Shape.ROCK
    if shape == 'B' or shape == 'Y': return Shape.PAPER
    if shape == 'C' or shape == 'Z': return Shape.SCISSORS

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
        score += player.value
    return score

def won(player, opponent):
    return ((player == Shape.ROCK and opponent == Shape.SCISSORS) or 
        (player == Shape.PAPER and opponent == Shape.ROCK) or
        (player == Shape.SCISSORS and opponent == Shape.PAPER))

def draw(player, opponent):
    return player == opponent

path = '2022/day_2_rock_paper_scissors/encrypted_strategy_guide.txt'
print(decrypt_strategy_guide(path))