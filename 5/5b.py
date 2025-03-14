import sys

def checkRules(pages,rules):
    pagesList = pages.split(',')
    outOfOrderFlag = 0
    checkAgainFlag = 1

    while(checkAgainFlag):
        for rule in rules:
            if(rule[0] in pagesList and rule[1] in pagesList):
                index1 = pagesList.index(rule[0])
                index2 = pagesList.index(rule[1])
                if(index1>index2):
                    print("following page are out of order, fixing")
                    pagesList[index1], pagesList[index2] = pagesList[index2], pagesList[index1]
                    print("list is now")
                    print(pagesList)
                    outOfOrderFlag = 1
                    checkAgainFlag = 1
                    break
        else:
            checkAgainFlag = 0
    if outOfOrderFlag:
        return int(middle_of_list(pagesList))
    else:
        print("following pages are already in order")
        print(pagesList)
        return 0
def middle_of_list(lst):
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return lst[n // 2 - 1:n // 2 + 1]

def main():
    with open('input.txt') as f:
        linecount = sum(1 for _ in f)
    #print(linecount)
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    rules = lines[:lines.index('')]
    updates = lines[lines.index('')+1:]
    count = 0
    splitRules = list(map(lambda x: x.split('|'),rules))
    for pages in updates:
        count = count + checkRules(pages,splitRules)
    print("count is:")
    print(count)


if __name__ == "__main__":
    main()
