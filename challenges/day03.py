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
    points = list()
    x = 0
    y = 0
    for line in lines:
        if line.direction == 'U':
            for i in range(0, line.length):
                y += 1
                points.append((x, y))
        elif line.direction == 'D':
            for i in range(0, line.length):
                y -= 1
                points.append((x, y))
        elif line.direction == 'L':
            for i in range(0, line.length):
                x -= 1
                points.append((x, y))
        elif line.direction == 'R':
            for i in range(0, line.length):
                x += 1
                points.append((x, y))
    return points


# TODO: not very generic yet (works only for 2)
def get_intersections(wire_points):
    return set(wire_points[0]).intersection(set(wire_points[1]))


def get_manhattan_dist(intersection):
    return abs(intersection[0]) + abs(intersection[1])


def get_step_count(points1, points2, intersection):
    index1 = points1.index(intersection)
    index2 = points2.index(intersection)
    return index1 + 1 + index2 + 1


class Day03(Challenge):
    input_file = 'inputs/day03.txt'

    def part1(self):
        all_wires = self.get_wires()
        wire_points = list()
        for wire in all_wires:
            lines = get_lines(wire)
            points = get_points(lines)
            wire_points.append(points)
        intersections = get_intersections(wire_points)
        manhattan_dists = [get_manhattan_dist(i) for i in intersections]
        self.print_result(min(manhattan_dists))

    def part2(self):
        all_wires = self.get_wires()
        lines1 = get_lines(all_wires[0])
        lines2 = get_lines(all_wires[1])
        step_list = list()
        for i in range(1, max(len(lines1), len(lines2))):
            points1 = get_points(lines1[:i])
            points2 = get_points(lines2[:i])
            intersections = get_intersections([points1, points2])
            if len(intersections) > 0:
                step_list.append(get_step_count(points1, points2, list(intersections)[0]))

        self.print_result(min(step_list))

    def get_wires(self):
        with open(self.input_file) as f:
            all_wires = f.readlines()
        all_wires = [w.strip() for w in all_wires]
        return all_wires
