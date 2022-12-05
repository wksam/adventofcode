def read_file(path):
    return open(path).read()

def format_input(input):
    return [[[int(number) for number in section.split('-')] for section in pair.split(',')] for pair in input.splitlines()]

def assignment_pairs_fully_contain(path):
    file = read_file(path)
    assignment_pairs = format_input(file)
    
    count = 0
    for pair in assignment_pairs:
        elf_1 = get_section(pair[0][0], pair[0][1])
        elf_2 = get_section(pair[1][0], pair[1][1])
        count += 1 if overlap(elf_1, elf_2) else 0
    return count

def get_section(begin, end):
    section = []
    for i in range(begin, end + 1):
        section.append(i)
    return section

def overlap(array_1, array_2):
    for i in array_1:
        if i in array_2:
            return True
    return False

path = '2022/day_4_camp_cleanup/assignments.txt'
print(assignment_pairs_fully_contain(path))