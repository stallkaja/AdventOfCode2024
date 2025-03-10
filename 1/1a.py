import sys


def main():

    with open('input.txt') as f:
        linecount = sum(1 for _ in f)
    #print(linecount)
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])

    left = []
    right = []
    total = 0;
    for line in lines:
        left.append(int(line.split(' ')[0]))
        right.append(int(line.split(' ')[3]))
    left.sort()
    right.sort()

    for i in range(0, len(left)):
        total += abs(left[i]-right[i])
    print(total)



if __name__ == "__main__":
    main()
