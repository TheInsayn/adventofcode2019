import inspect


class Challenge:
    input_file = None

    def part1(self): raise NotImplementedError

    def part2(self): raise NotImplementedError

    def print_result(self, result):
        print("[{0}_{1}]: result is: {2}".format(self.__class__.__name__, inspect.stack()[1].function, result))
