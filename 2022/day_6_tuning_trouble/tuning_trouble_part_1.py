def read_file(path):
    return open(path).read()

def start_of_packet_marker(path):
    datastream = read_file(path)

    stream = []
    position = 0
    while position < len(datastream):
        char = datastream[position]
        if char not in stream:
            stream.append(char)
            if len(stream) == 4:
                position += 1
                break
        else:
            stream.reverse()
            position -= stream.index(char)
            stream = []
            stream.append(datastream[position])
        position += 1
    
    return position

path = '2022/day_6_tuning_trouble/datastream_buffer.txt'
print(start_of_packet_marker(path))