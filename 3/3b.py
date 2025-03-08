import sys

import re


def multiply(input):
    input = input[4:-1]
    digits = input.split(',')
    print(digits)
    return int(digits[0]) * int(digits[1])


def main():
    with open('input.txt') as f:
        linecount = sum(1 for _ in f)
    # print(linecount)
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])
    print(lines)
    print(lines[0])
    print(lines[1])
    input = ""
    for line in lines:
        input = input + line

    # mul[(]\d{1,3}\,\d{1,3}[)] regex to match for mul(x,y) where x and y can be up to three digits
    pattern = r"mul[(]\d{1,3}\,\d{1,3}[)]|do[(][)]|don[']t[(][)]"
    ops = re.findall(pattern, input)
    total = 0
    toggle = 1;
    for op in ops:
        print("curent op is " + op)
        if toggle == 1 and op == "don't()":
            toggle = 0
        elif toggle == 0 and op == "do()":
            toggle = 1
        if (op != "don't()" and op != "do()") and toggle == 1:
            total = total + multiply(op)
    print(total)


if __name__ == "__main__":
    main()
