import sys

def optimal_summands(n):
    summands = []
    #write your code here
    difference = n
    curr = 1
    while difference > 0:
        if difference - curr <= curr:
            curr = difference

        summands.append(curr)
        difference -= curr
        curr += 1

    return summands

if __name__ == '__main__':
    input = input()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
