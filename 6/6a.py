import sys


def findLocation(curDirection, lines):
    for i in range(0, len(lines)):
        try:
            return [i, lines[i].index(curDirection)]
        except:
            pass


def main():
    with open('input.txt') as f:
        linecount = sum(1 for _ in f)
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])

    map = []
    for line in lines:
        newLine = list(line)
        map.append(newLine)
    curDirection = "^"
    curLoc = findLocation(curDirection, map)
    moving = 1
    maxy = len(lines)
    maxx = len(lines[0])
    count = 0
    while (moving):
        map[curLoc[0]][curLoc[1]] = 'X'
        y = curLoc[0]
        x = curLoc[1]
        if y - 1 >= 0 and curDirection == "^":
            if map[y - 1][x] == "#":
                curDirection = ">"
            elif map[y - 1][x] == "." or map[y - 1][x] == "X":
                curLoc[0] = curLoc[0] - 1
            else:
                print("error")
        elif x + 1 < maxx and curDirection == ">":
            if map[y][x + 1] == "#":
                curDirection = "v"
            elif map[y][x + 1] == "." or map[y][x + 1] == "X":
                curLoc[1] = curLoc[1] + 1
            else:
                print("error")
        elif y + 1 < maxy and curDirection == "v":
            if map[y + 1][x] == "#":
                curDirection = "<"
            elif map[y + 1][x] == "." or map[y + 1][x] == "X":
                curLoc[0] = curLoc[0] + 1
            else:
                print("error")
        elif x - 1 >= 0 and curDirection == "<":
            if map[y][x-1] == "#":
                curDirection = "^"
            elif map[y][x-1] == "." or map[y][x-1] == "X":
                curLoc[1] = curLoc[1] - 1
            else:
                print("error")
        else:
            moving = 0

    for line in map:
        count = count + line.count("X")
        print(line)
    print(count)
    print(curDirection)


if __name__ == "__main__":
    main()
