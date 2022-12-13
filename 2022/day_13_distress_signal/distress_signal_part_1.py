def read_file(path):
    return open(path).read()

def format_input(file):
    return [[eval(packet) for packet in pairs.split('\n')] for pairs in file.split('\n\n')]

def decode_message(path):
    file = read_file(path)
    packets = format_input(file)

    sum = 0
    for index, packet in enumerate(packets):
        [left, right] = packet
        if (is_right_order(left, right) != -1):
            sum += index + 1
    return sum

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

path = '2022/day_13_distress_signal/received_packets.txt'
print(decode_message(path))