class Challenge:

    def part1(self): raise NotImplementedError

    def part2(self): raise NotImplementedError

    def print_result(self, result):
        print("{0}: result is: {1}".format(self.__class__.__name__, result))
