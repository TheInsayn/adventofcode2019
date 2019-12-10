from challenges.challenge import Challenge


class Day01(Challenge):
    input_file = 'inputs/day01.txt'

    def part1(self):
        total = 0
        with open(self.input_file, 'r') as f:
            for i in f.readlines():
                number = int(i)
                total = total + int(number / 3) - 2
        self.print_result(total)

        # alternative
        # total = sum([int(int(i) / 3) - 2 for i in open(self.input_file, 'r').readlines()])
        # self.print_result(total)

    def part2(self):
        total = 0
        with open(self.input_file, 'r') as f:
            for i in f.readlines():
                number = int(i)
                total = total + self.part2_rec(number)
        self.print_result(total)

    def part2_rec(self, fuel):
        required = int(fuel / 3) - 2
        if required <= 0:
            return 0
        else:
            return required + self.part2_rec(required)
