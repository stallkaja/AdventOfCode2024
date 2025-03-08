import sys



def dampenedLinkCheck(line):
    for i in range(0, len(line)):
        newline = [x for index, x in enumerate(line) if index != i]
        if lineCheck(newline):
            return 1
    return 0
def lineCheck(line):
    for i in range(0, len(line) - 1):
        if abs(int(line[i]) - int(line[i + 1])) > 3 or abs(int(line[i]) - int(line[i + 1])) < 1:
            # found instance where levels differ by at less one or more than three. Not safe
            # print("too big of change")
            return 0
        if int(line[0]) < int(line[1]):
            # increasing, need to check if safe
            if (i < len(line)) and int(line[i]) > int(line[i + 1]):
                # found instance of next decreasing, means not safe
                # print("found decreasing when all should increase")
                return 0
        if int(line[0]) > int(line[1]):
            # decreasing, need to check if safe
            if (i < len(line)) and int(line[i]) < int(line[i + 1]):
                # found instance of next increasing, meas not safe
                # print("found increasing when all should decrease")
                return 0

        if int(line[0]) == int(line[1]):
            # print("found equal")
            return 0

            # means they are equal mean not safe
    return 1
def main():
    with open('input.txt') as f:
        linecount = sum(1 for _ in f)
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])
    count = 0
    for line in lines:
        line = line.split(' ')
        if lineCheck(line):
            #if we get here then all the safety checks passed and the line should be safe.
            print(str(line) + "Is safe")
            count = count + 1
        elif dampenedLinkCheck(line):
            print("line safe after remove")
            print(str(line) + "Is safe")
            count = count + 1
        else:
            # if we got here then at least one of the safety checks failed and the line is not safe.
            print(str(line) + "Isnt safe")
        print("sum is " + str(count))
if __name__ == "__main__":
    main()
