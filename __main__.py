from challenges.day01 import Day1
from challenges.day02 import Day2
from challenges.day03 import Day3


def call_parts(challenge):
    challenge.part1()
    challenge.part2()


def main():
    call_parts(Day1())
    call_parts(Day2())
    call_parts(Day3())


if __name__ == "__main__":
    main()
