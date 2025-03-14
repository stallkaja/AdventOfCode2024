import sys

def checkRules(pages,rules):
    for rule in rules:
        if(rule[0] in pages and rule[1] in pages):
            index1 = pages.index(rule[0])
            index2 = pages.index(rule[1])
            if(index1>index2):
                print("following page are out of order")
                print(pages)
                return 0
    print("following pages are in order")
    print(pages)
    return 1
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
        if(checkRules(pages,splitRules)):
            count = count + int(middle_of_list(pages))
    print("count is:")
    print(count)



if __name__ == "__main__":
    main()
