import string

class Node:
    def __init__(self, height, parent=None, position=None) -> None:
        self.parent = parent
        self.position = position
        self.g_cost = 0
        self.f_cost = 0
        self.h_cost = 0
        self.height = height

def read_file(path):
    return open(path).read()

def format_input(file):
    return [list(line) for line in file.splitlines()]

def pathfinder(file):
    file = read_file(path)
    heightmap = format_input(file)
    [start_position, end_position] = extract_start_end_and_convert(heightmap)
    node = astar(heightmap, start_position, end_position)
    return node.f_cost

def convert_height(element):
    return string.ascii_lowercase.index(element)

def extract_start_end_and_convert(heightmap):
    start_position = end_position = []
    for y, line in enumerate(heightmap):
        for x, element in enumerate(line):
            if element == 'S':
                start_position = [x, y]
                heightmap[y][x] = 'a'
            elif element == 'E':
                end_position = [x, y]
                heightmap[y][x] = 'z'
            heightmap[y][x] = convert_height(heightmap[y][x])
    return [start_position, end_position]

def astar(heightmap, start, end):
    start_node = Node(convert_height('a'), position=start)
    end_node = Node(convert_height('z'), position=end)
    
    open_list = [start_node]
    closed_list = []

    while len(open_list) > 0:
        current_node = get_lowest_f_cost(open_list)
        closed_list.append(current_node)
        if current_node.position == end_node.position:
            return current_node
        for neighbor in get_neighbors(current_node, heightmap):
            if is_in_the_list(neighbor, closed_list):
                continue
            neighbor.g_cost = current_node.g_cost + 1
            neighbor.h_cost = abs(end_node.position[0] - neighbor.position[0]) + abs(end_node.position[1] - neighbor.position[1])
            neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
            if is_in_the_list(neighbor, open_list):
                continue
            open_list.append(neighbor)
    return

def is_in_the_list(node, list):
    return any(list_node.position == node.position for list_node in list)

def get_lowest_f_cost(nodes):
    nodes.sort(key=lambda node: node.f_cost)
    return nodes.pop(0)

def get_neighbors(node, heightmap):
    [x, y] = node.position
    neighbors = []
    for position in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        neighbor_position = [x + y for x, y in zip(position, node.position)]
        if neighbor_position[0] >= len(heightmap[0]) or neighbor_position[0] < 0 or neighbor_position[1] >= len(heightmap) or neighbor_position[1] < 0:
            continue
        [nx, ny] = neighbor_position
        if heightmap[ny][nx] > (heightmap[y][x] + 1):
            continue
        neighbors.append(Node(heightmap[y][x], node, neighbor_position))
    return neighbors

path = '2022/day_12_hill_climbing_algorithm/heightmap.txt'
print(pathfinder(path))