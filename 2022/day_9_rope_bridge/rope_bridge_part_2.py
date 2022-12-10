import math

def read_file(path):
    return open(path).read()

def format_input(input):
    return input.splitlines()

def tail_tracker(path):
    file = read_file(path)
    motions = format_input(file)

    d = ['U', 'D', 'R', 'L']
    m = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    head = [0, 0]
    tails = [[0, 0]] * 9

    last_tail_path = [[0, 0]]
    for motion in motions:
        [direction, magnitude] = motion.split(' ')
        move_head = m[d.index(direction)]
        for _ in range(int(magnitude)):
            head = [x + y for x, y in zip(move_head, head)]
            for t in range(len(tails)):
                tail_head = head
                tail = tails[t]
                if t > 0:
                    tail_head = tails[t - 1]
                    tail = tails[t]
                if is_not_touching(tail_head, tail):
                    move_tail = [round_up((x - y) / 2) for x, y in zip(tail_head, tail)]
                    tails[t] = [x + y for x, y in zip(move_tail, tail)]
                    if t == len(tails) - 1:
                        last_tail_path.append(tails[t])
                else:
                    break
    return len(list(set([tuple(position) for position in last_tail_path])))

def is_not_touching(head, tail):
    return abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1

def round_up(number):
    return int(math.ceil(abs(number)) * (abs(number) / number)) if number != 0 else 0

path = '2022/day_9_rope_bridge/series_of_motions.txt'
print(tail_tracker(path))