def read_file(path):
    return open(path).read()

def format_input(file):
    sanitized_input = file.replace('Sensor at x=', '').replace(' closest beacon is at x=', '').replace(' y=', '')
    return [[[int(coord) for coord in position.split(',')] for position in line.split(':')] for line in sanitized_input.splitlines()]

def beacon_exclusion_zone(path):
    file = read_file(path)
    report = format_input(file)
    distances = [manhattan_geometry(coords[0], coords[1]) for coords in report]
    no_beacon_counter = count_no_beacon_in_range(report, distances, 2000000)
    return no_beacon_counter

def manhattan_geometry(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_no_beacon_line(sensor, d, y):
    right_x = d - abs(y - sensor[1]) + sensor[0]
    left_x = (sensor[0] - right_x) * 2 + right_x
    return [left_x, right_x]

def count_no_beacon_in_range(report, distances, distance_y):
    no_beacon_ranges = []
    beacons_range = set()
    for index, [sensor, beacon] in enumerate(report):
        if distance_y <= sensor[1] + distances[index] and distance_y >= sensor[1] - distances[index]:
            no_beacon_ranges.append(get_no_beacon_line(sensor, distances[index], distance_y))
            if beacon[1] == distance_y:
                beacons_range.add(tuple(beacon))
    min_x = min(no_beacon_ranges, key=lambda x: x[0])
    max_x = max(no_beacon_ranges, key=lambda x: x[1])
    return abs(min_x[0] - max_x[1]) + 1 - len(beacons_range)

path = '2022/day_15_beacon_exclusion_zone/sensors_report.txt'
print(beacon_exclusion_zone(path))

# 5543956 too high
# 4502209 too high