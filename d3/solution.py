import sys

file = open("input.txt", 'r')

priorities = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26,
    'A':27,
    'B':28,
    'C':29,
    'D':30,
    'E':31,
    'F':32,
    'G':33,
    'H':34,
    'I':35,
    'J':36,
    'K':37,
    'L':38,
    'M':39,
    'N':40,
    'O':41,
    'P':42,
    'Q':43,
    'R':44,
    'S':45,
    'T':46,
    'U':47,
    'V':48,
    'W':49,
    'X':50,
    'Y':51,
    'Z':52
}

def part1():
    sum_of_priorities = 0
    for line in file:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        # find the leeter that is in both halves
        for letter in first_half:
            if letter in second_half:
                sum_of_priorities += priorities[letter]
                break
    print(sum_of_priorities)

def part2():
    sum_of_priorities = 0

    for line1, line2, line3 in zip(file, file, file):
        for letter in line1:
            if letter in line2 and letter in line3:
                sum_of_priorities += priorities[letter]
                break
    print(sum_of_priorities)

if __name__ == "__main__":
    #part1()
    part2()