from challenges.challenge import Challenge


class Day2(Challenge):
    input_file = 'inputs/day02.txt'

    def part1(self, noun=12, verb=2, wanted=None):
        with open(self.input_file, 'r') as f:
            codes = [int(i) for i in f.readline().split(',')]
        codes[1] = noun
        codes[2] = verb
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

            if codes[store] == wanted:
                return True
        if wanted is None:
            self.print_result(codes[0])
        else:
            return False

    def part2(self):
        wanted = 19690720
        op_max = 99
        for noun in range(0, op_max + 1):
            for verb in range(0, op_max + 1):
                match = self.part1(noun, verb, wanted)
                if match:
                    self.print_result(100 * noun + verb)
                    return
        self.print_result("none")
