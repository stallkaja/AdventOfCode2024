import sys


def checkNeighbors(x, y, lines):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < len(lines) and 0 <= y + j < len(lines[x]) and lines[x + i][y + j] == 'M':
                if 0 <= x + i + i < len(lines) and 0 <= y + j + j < len(lines[x]) and lines[x + i + i][y + j + j] == 'A':
                    if 0 <= x + i + i + i < len(lines) and 0 <= y + j + j + j < len(lines[x]) and lines[x + i + i + i][y + j + j + j] == 'S':
                        print("found an M at:" + str(x + i) + ' ' + str(y + j))
                        print("found an A at:" + str(x + i + i) + ' ' + str(y + j + j))
                        print("found an S at:" + str(x + i + i + i) + ' ' + str(y + j + j + j))
                        print("Found XMAS")
                        count = count + 1
    return count


def main():
    with open('input.txt') as f:
        linecount = sum(1 for _ in f)
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    count = 0

    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == 'X':
                print("found an x at:" + str(i) + ' ' + str(j))

                count = count + checkNeighbors(i, j, lines)
    print(count)


if __name__ == "__main__":
    main()
