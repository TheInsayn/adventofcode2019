from challenges.challenge import Challenge


class Line:
    def __init__(self, direction, length):
        self.direction = direction
        self.length = int(length)

    def __str__(self):
        return "[{0}, {1}]".format(self.direction, self.length)


def get_line(w):
    return Line(w[0], w[1:])


def get_lines(wire):
    lines = list()
    for w in wire.split(','):
        line = get_line(w)
        lines.append(line)
    return lines


def get_points(lines):
    points = set()
    x = 0
    y = 0
    for line in lines:
        if line.direction == 'U':
            for i in range(0, line.length):
                y += 1
                points.add((x, y))
        elif line.direction == 'D':
            for i in range(0, line.length):
                y -= 1
                points.add((x, y))
        elif line.direction == 'L':
            for i in range(0, line.length):
                x -= 1
                points.add((x, y))
        elif line.direction == 'R':
            for i in range(0, line.length):
                x += 1
                points.add((x, y))
    return points


def get_intersections(wire_points):
    return wire_points[0].intersection(wire_points[1])


def get_manhattan_dist(intersection):
    return abs(intersection[0]) + abs(intersection[1])


class Day3(Challenge):
    input_file = 'inputs/day03.txt'

    def part1(self):
        with open(self.input_file) as f:
            all_wires = f.readlines()
        all_wires = [w.strip() for w in all_wires]
        wire_points = list()
        for wire in all_wires:
            lines = get_lines(wire)
            points = get_points(lines)
            wire_points.append(points)
        intersections = get_intersections(wire_points)
        # print("intersections:", intersections)
        manhattan_dists = [get_manhattan_dist(i) for i in intersections]
        # print("manhattan distances:", manhattan_dists)
        # print("minimum:", min(manhattan_dists))
        self.print_result(min(manhattan_dists))

    def part2(self):
        pass
