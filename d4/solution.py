import sys

file = open("input.txt", "r")

def part1():

    fully_contained = 0

    for line in file:
        array1, array2 = line.split(",")

        array1 = list(range(int(array1.split("-")[0]), int(array1.split("-")[1]) + 1))
        array2 = list(range(int(array2.split("-")[0]), int(array2.split("-")[1]) + 1))

        if set(array1).issubset(array2) or set(array2).issubset(array1):
            fully_contained += 1

    print(fully_contained)

def part2():
    pass

if __name__ == '__main__':
    part1()
    part2()
