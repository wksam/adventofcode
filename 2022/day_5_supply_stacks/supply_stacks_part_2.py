def read_file(path):
    return open(path).read()

def format_input(input):
    crates, steps = input.split('\n\n')

    stacks = format_stacks(crates)
    procedure = format_procedure(steps)

    return stacks, procedure

def format_stacks(crates):
    crates = crates.splitlines()
    crates.reverse()
    stacks = []
    for level in crates:
        stack = 0
        for i in range(1, len(level), 4):
            if level[i].isdigit():
                stacks.append([])
            elif level[i] != ' ':
                stacks[stack].append(level[i])
            stack += 1
    return stacks

def format_procedure(steps):
    steps = [[int(s) for s in step.split() if s.isdigit()] for step in steps.splitlines()]
    for step in steps:
        step[1] -= 1
        step[2] -= 1
    return steps

def rearrangement_procedure(path):
    file = read_file(path)
    stacks, procedure = format_input(file)

    for command in procedure:
        quantity, from_stack, to_stack = command
        crates = stacks[from_stack][len(stacks[from_stack]) - quantity:]
        del stacks[from_stack][len(stacks[from_stack]) - quantity:]
        stacks[to_stack] += crates

    on_top_crates = ''
    for stack in stacks:
        on_top_crates += stack.pop()
    
    return on_top_crates

path = '2022/day_5_supply_stacks/stacks_and_procedure.txt'
print(rearrangement_procedure(path))