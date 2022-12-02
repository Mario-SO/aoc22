import sys

file = open('input.txt', 'r')

# ------
# Part 1
# ------

# ----------------
# My choices
# ----------------
# X = Rock -> +1
# Y = paper -> +2
# Z = Scissors -> +3

# ----------------
# Opponent choices
# ----------------
# A = Rock
# B = Paper
# C = Scissors

# ----------------
# Results
# ----------------
# Draw = +3
# Win = +6
# Lose = 0

def part1():
    result = 0

    for line in file:
        if line[2] == 'X' and line[0] == 'A':
            result += 4
        if line[2] == 'Y' and line[0] == 'B':
            result += 5
        if line[2] == 'Z' and line[0] == 'C':
            result += 6
        if line[2] == 'X' and line[0] == 'B':
            result += 1
        if line[2] == 'Y' and line[0] == 'C':
            result += 2
        if line[2] == 'Z' and line[0] == 'A':
            result += 3
        if line[2] == 'X' and line[0] == 'C':
            result += 7
        if line[2] == 'Y' and line[0] == 'A':
            result += 8
        if line[2] == 'Z' and line[0] == 'B':
            result += 9

    print(result)

# ------
# Part 2
# ------

# ----------------
# Results
# ----------------
# Draw = Y = +3
# Win = Z = +6
# Lose = X = +0


def part2():
    result = 0

    for line in file:
        if line[2] == 'X' and line[0] == 'A':
            result += 3
        if line[2] == 'Y' and line[0] == 'B':
            result += 5
        if line[2] == 'Z' and line[0] == 'C':
            result += 7
        if line[2] == 'X' and line[0] == 'B':
            result += 1
        if line[2] == 'Y' and line[0] == 'C':
            result += 6
        if line[2] == 'Z' and line[0] == 'A':
            result += 8
        if line[2] == 'X' and line[0] == 'C':
            result += 2
        if line[2] == 'Y' and line[0] == 'A':
            result += 4
        if line[2] == 'Z' and line[0] == 'B':
            result += 9

    print(result)

if __name__ == '__main__':
    part1()
    #part2()
