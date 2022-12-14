def read_file(path):
    return open(path).read()

def format_input(file):
    return [[eval(packet) for packet in pairs.split('\n')] for pairs in file.split('\n\n')]

def decode_message(path):
    file = read_file(path)
    packets = format_input(file)
    packets.append([[[2]], [[6]]])
    packets = flat(packets)
    packets = quicksort(packets)
    [divider1, divider2] = find_divider_packets(packets)
    return divider1 * divider2

def is_right_order(left, right):
    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
    
    if isinstance(left, list) and isinstance(right, list):
        index = 0
        while index < len(left) and index < len(right):
            comparison = is_right_order(left[index], right[index])
            if comparison == 1:
                return 1
            if comparison == -1:
                return -1
            index += 1
        if index == len(left):
            if index == len(right):
                return 0
            return 1
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        if left == right:
            return 0
    return -1

def quicksort(list):
    lower = []
    higher = []
    
    if len(list) == 0:
        return list

    pivot = list.pop(0)
    for item in list:
        if is_right_order(item, pivot) != -1:
            lower.append(item)
        else:
            higher.append(item)
    return quicksort(lower) + [pivot] + quicksort(higher)

def find_divider_packets(packets):
    divider1 = divider2 = 0
    for i, packet in enumerate(packets):
        if packet == [[2]]:
            divider1 = i + 1
        elif packet == [[6]]:
            divider2 = i + 1
    return [divider1, divider2]

def flat(list):
    return [item for sublist in list for item in sublist]

path = '2022/day_13_distress_signal/received_packets.txt'
print(decode_message(path))