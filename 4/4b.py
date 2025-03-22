import sys


def check_neighbors(y, x, max_y, max_x, lines):
    if x - 1 >= 0 and y - 1 >= 0 and (lines[y - 1][x - 1] == "M" or lines[y - 1][x - 1] == "S"):
        corner = lines[y - 1][x - 1]
        print("upper left corner found")
        if corner == "M":
            if y + 1 < max_y and x + 1 < max_x and lines[y + 1][x + 1] == "S":
                print("opposite corner is good.")
                if y - 1 >= 0 and x + 1 < max_x and (lines[y - 1][x + 1] == "M" or lines[y - 1][x + 1] == "S"):
                    right_corner = lines[y - 1][x + 1]
                    print("upper right is good")
                    if right_corner == "M":
                        if y + 1 < max_y and x - 1 >= 0 and lines[y + 1][x - 1] == "S":
                            print("lower left is good")
                            return 1
                    if right_corner == "S":
                        if y + 1 < max_y and x - 1 >= 0 and lines[y + 1][x - 1] == "M":
                            print("lower left is good")
                            return 1
        if corner == "S":
            if y + 1 < max_y and x + 1 < max_x and lines[y + 1][x + 1] == "M":
                print("opposite corner is good.")
                if y - 1 >= 0 and x + 1 < max_x and (lines[y - 1][x + 1] == "M" or lines[y - 1][x + 1] == "S"):
                    right_corner = lines[y - 1][x + 1]
                    print("upper right is good")
                    if right_corner == "M":
                        if y + 1 < max_y and x - 1 >= 0 and lines[y + 1][x - 1] == "S":
                            print("lower left is good")
                            return 1
                    if right_corner == "S":
                        if y + 1 < max_y and x - 1 >= 0 and lines[y + 1][x - 1] == "M":
                            print("lower left is good")
                            return 1


    return 0


def main():
    with open('input.txt') as f:
        linecount = sum(1 for _ in f)
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    count = 0

    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == 'A':
                print("found an A at:" + str(i) + ' ' + str(j))
                count = count + check_neighbors(i, j, len(lines), len(lines[i]), lines, )
    print(count)


if __name__ == "__main__":
    main()
