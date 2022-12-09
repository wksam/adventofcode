def read_file(path):
    return open(path).read()

def format_input(input):
    return [[int(tree) for tree in list(line)] for line in input.splitlines()]

def visible_trees(path):
    file = read_file(path)
    trees = format_input(file)

    scores = []
    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[y]) - 1):
            # Top
            visible_trees = 0
            for tree in reversed([row[x] for row in trees][:y]):
                visible_trees += 1
                if tree >= trees[y][x]:
                    break
            score = visible_trees

            # Bottom
            visible_trees = 0
            for tree in [row[x] for row in trees][y + 1:]:
                visible_trees += 1
                if tree >= trees[y][x]:
                    break
            score *= visible_trees

            # Left
            visible_trees = 0
            for tree in reversed(trees[y][:x]):
                visible_trees += 1
                if tree >= trees[y][x]:
                    break
            score *= visible_trees

            # Right
            visible_trees = 0
            for tree in trees[y][x + 1:]:
                visible_trees += 1
                if tree >= trees[y][x]:
                    break
            score *= visible_trees
            
            scores.append(score)
    return max(scores)

path = '2022/day_8_treetop_tree_house/trees_height.txt'
print(visible_trees(path))