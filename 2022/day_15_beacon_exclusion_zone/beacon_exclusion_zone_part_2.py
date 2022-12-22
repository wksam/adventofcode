def read_file(path):
    return open(path).read()

def format_input(file):
    sanitized_input = file.replace('Sensor at x=', '').replace(' closest beacon is at x=', '').replace(' y=', '')
    return [[[int(coord) for coord in position.split(',')] for position in line.split(':')] for line in sanitized_input.splitlines()]

def beacon_exclusion_zone(path):
    file = read_file(path)
    report = format_input(file)
    report = [(coord[0], coord[1], manhattan_geometry(coord[0], coord[1])) for coord in report]
    for sensor_1, _, distance_1 in report:
        for distance_x in range(distance_1 + 2):
            distance_y = distance_1 + 1 - distance_x
            for x, y in [(sensor_1[0] + distance_x, sensor_1[1] + distance_y), (sensor_1[0] + distance_x, sensor_1[1] - distance_y), (sensor_1[0] - distance_x, sensor_1[1] + distance_y), (sensor_1[0] - distance_x, sensor_1[1] - distance_y)]:
                if x < 0 or x > 4000000 or y < 0 or y > 4000000:
                    continue
                if is_not_in_range(x, y, report):
                    return 4000000 * x + y
    return report

def manhattan_geometry(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_not_in_range(x, y, report):
    for sensor, _, distance in report:
        if(manhattan_geometry(sensor, [x, y])) <= distance:
            return False
    return True

path = '2022/day_15_beacon_exclusion_zone/sensors_report.txt'
print(beacon_exclusion_zone(path))