def read_file(path):
    return open(path).read()

def format_input(file):
    return [[[int(coordinate) for coordinate in position.split(',')] for position in line.split(' -> ')] for line in file.splitlines()]

def regolith_reservoir(path):
    file = read_file(path)
    rocks = format_input(file)
    filled_spaces = fill_rocks(rocks)
    steps = simulate_sand(filled_spaces, get_boundary_y(rocks))
    return steps

def get_boundary_y(rocks):
    y = [coords[1] for rock in rocks for coords in rock]
    return max(y)

def fill_rocks(rocks):
    filled_spaces = set()
    for rock in rocks:
        start = []
        for coords in rock:
            if not start:
                start = coords
                continue
            if start[0] == coords[0]:
                for y in range(min(start[1], coords[1]), max(start[1], coords[1]) + 1):
                    filled_spaces.add(tuple([start[0], y]))
            elif start[1] == coords[1]:
                for x in range(min(start[0], coords[0]), max(start[0], coords[0]) + 1):
                    filled_spaces.add(tuple([x, start[1]]))
            start = coords
    return filled_spaces

def simulate_sand(filled_spaces, max_y):
    sand_respawn = [sand_x, sand_y] = [500, 0]
    sand_counter = 0
    while sand_y <= max_y:
        if (sand_x, sand_y + 1) not in filled_spaces:
            sand_y += 1
            continue
        if (sand_x - 1, sand_y + 1) not in filled_spaces:
            sand_x -= 1
            sand_y += 1
            continue
        if (sand_x + 1, sand_y + 1) not in filled_spaces:
            sand_x += 1
            sand_y += 1
            continue
        filled_spaces.add((sand_x, sand_y))
        sand_counter += 1
        [sand_x, sand_y] = sand_respawn
    return sand_counter

path = '2022/day_14_regolith_reservoir/cave_scan.txt'
print(regolith_reservoir(path))