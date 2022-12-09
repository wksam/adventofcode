def read_file(path):
    return open(path).read()

def format_input(input):
    return [[int(tree) for tree in list(line)] for line in input.splitlines()]

def visible_trees(path):
    file = read_file(path)
    trees = format_input(file)

    visible = len(trees) * 2 + len(trees[0]) * 2 - 4
    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[y]) - 1):
            # Top
            if max([row[x] for row in trees][:y]) < trees[y][x]:
                visible += 1
            # Bottom
            elif max([row[x] for row in trees][y + 1:]) < trees[y][x]:
                visible += 1
            # Left
            elif max(trees[y][:x]) < trees[y][x]:
                visible += 1
            # Right
            elif max(trees[y][x + 1:]) < trees[y][x]:
                visible += 1
    return visible

path = '2022/day_8_treetop_tree_house/trees_height.txt'
print(visible_trees(path))