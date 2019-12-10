from challenges.day01 import Day01
from challenges.day02 import Day02
from challenges.day03 import Day03
from challenges.day04 import Day04


def call_parts(challenge):
    challenge.part1()
    challenge.part2()


def main():
    # call_parts(Day01())
    # call_parts(Day02())
    # call_parts(Day03())
    call_parts(Day04())


if __name__ == "__main__":
    main()
