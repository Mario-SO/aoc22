import sys

file = open('input.txt', 'r')

# ------
# Part 1
# ------

def part1():
    current_biggest_sum = 0
    current_sum = 0

    for line in file:
        if line != '\n':
            current_sum += int(line)
            if current_sum > current_biggest_sum:
                current_biggest_sum = current_sum
        else:
            current_sum = 0

    print(current_biggest_sum)

# ------
# Part 2
# ------

def part2():
    all_sums = []
    current_sum = 0

    for line in file:
        if line != '\n':
            current_sum += int(line)
        else:
            all_sums.append(current_sum)
            current_sum = 0

    print(sum(sorted(all_sums, reverse=True)[:3]))

if __name__ == '__main__':
    part2()
