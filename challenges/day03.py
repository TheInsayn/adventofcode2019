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


def get_grid(max_size):
    rows = list()
    for line in range(0, max_size):
        rows.append('.' * max_size)
    return rows


def get_max_size(lines):
    return max(x.length for x in lines)


def fill_grid(grid, lines):
    # TODO
    pass


class Day3(Challenge):
    input_file = 'inputs/day03.txt'

    def part1(self):
        with open(self.input_file) as f:
            all_wires = f.readlines()
        all_wires = [w.strip() for w in all_wires]
        print(all_wires)
        for wire in all_wires:
            print(wire)
            lines = get_lines(wire)
            max_size = get_max_size(lines)
            grid = get_grid(max_size)
            print(grid)
            grid = fill_grid(grid, lines)

    def part2(self):
        pass
