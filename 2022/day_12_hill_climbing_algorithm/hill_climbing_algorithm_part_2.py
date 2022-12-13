import string

class Node:
    def __init__(self, position, steps=0, parent=None) -> None:
        self.position = position
        self.parent = parent
        self.steps = steps

def read_file(path):
    return open(path).read()

def format_input(file):
    return [list(line) for line in file.splitlines()]

def pathfinder(file):
    file = read_file(path)
    heightmap = format_input(file)
    start_position = extract_start_and_convert(heightmap)
    node = breadth_first_search(heightmap, start_position)
    return node.steps

def extract_start_and_convert(heightmap):
    start_position = []
    for y, line in enumerate(heightmap):
        for x, element in enumerate(line):
            if element == 'S':
                heightmap[y][x] = 'a'
            elif element == 'E':
                start_position = [x, y]
                heightmap[y][x] = 'z'
            heightmap[y][x] = convert_height(heightmap[y][x])
    return start_position

def convert_height(element):
    return string.ascii_lowercase.index(element)

def breadth_first_search(heightmap, start):
    explored = [Node(start)]
    queue = [Node(start)]
    while queue:
        current = queue.pop(0)
        [x, y] = current.position
        if heightmap[y][x] == 0:
            return current
        for neighbor in get_neighbors(current, heightmap):
            if not is_explored(neighbor.position, explored):
                explored.append(neighbor)
                queue.append(neighbor)

def is_explored(value, list):
    return any(element.position == value for element in list)

def get_neighbors(current, heightmap):
    [x, y] = current.position
    neighbors = []
    for position in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        neighbor_position = [x + y for x, y in zip(position, current.position)]
        if neighbor_position[0] >= len(heightmap[0]) or neighbor_position[0] < 0 or neighbor_position[1] >= len(heightmap) or neighbor_position[1] < 0:
            continue
        [nx, ny] = neighbor_position
        if heightmap[ny][nx] < heightmap[y][x] - 1:
            continue
        neighbors.append(Node(neighbor_position, current.steps + 1, current))
    return neighbors

path = '2022/day_12_hill_climbing_algorithm/heightmap.txt'
print(pathfinder(path))