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



    for i in range(0,len(left)):
        cnt = 0;
        for j in right:
            if left[i] == j:
                cnt+=1
        left[i] = left[i] * cnt
        total = total + left[i]
    print("Similar left")
    print(left)
    print(total)



if __name__ == "__main__":
    main()
