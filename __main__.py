def day01_1():
    total = 0
    with open('inputs/day01.txt', 'r') as f:
        for i in f.readlines():
            number = int(i)
            total = total + int(number / 3) - 2

    print(total)

    total = sum([int(int(i)/3)-2 for i in open('input.txt', 'r').readlines()])
    print(total)


def day01_2():
    total = 0
    with open('input.txt', 'r') as f:
        for i in f.readlines():
            number = int(i)
            total = total + day01_2_rec(number)

    print(total)


def day01_2_rec(fuel):
    required = int(fuel / 3) - 2
    if required <= 0:
        return 0
    else:
        return required + day01_2_rec(required)


def main():
    day01_1()
    day01_2()


if __name__ == "__main__":
    main()