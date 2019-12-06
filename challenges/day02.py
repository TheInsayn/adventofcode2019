from challenges.challenge import Challenge


class Day2(Challenge):
    input_file = 'inputs/day02.txt'

    def part1(self):
        with open(self.input_file, 'r') as f:
            codes = [int(i) for i in f.readline().split(',')]
        codes[1] = 12
        codes[2] = 2
        for i in range(0, len(codes), 4):
            op = codes[i + 0]
            if op == 99:
                break
            idx1 = codes[i + 1]
            idx2 = codes[i + 2]
            store = codes[i + 3]

            if op == 1:
                codes[store] = codes[idx1] + codes[idx2]
            elif op == 2:
                codes[store] = codes[idx1] * codes[idx2]

        self.print_result(codes[0])

    def part2(self):
        pass
