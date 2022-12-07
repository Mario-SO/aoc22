import sys

file = open("input.txt", 'r')

def part1():
# read first 6 lines and store in 9 different stacks
    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []
    stack5 = []
    stack6 = []
    stack7 = []
    stack8 = []
    stack9 = []
    for i in range(6):

        line = file.readline()
        line = line.strip()

        stack1.append(line[0])
        stack2.append(line[1])
        stack3.append(line[2])
        stack4.append(line[3])
        stack5.append(line[4])
        stack6.append(line[5])
        stack7.append(line[6])
        stack8.append(line[7])
        stack9.append(line[8])

    print(stack1)


if __name__ == "__main__":
    part1()
    #part2()
