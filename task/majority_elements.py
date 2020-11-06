# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    a = sorted(a)
    std = len(a)//2
    begin = left
    end = left
    while end < len(a):
        print(begin, end)
        print(end-begin+1, "std===> ", std)
        if a[end] != a[begin]:
            begin = end
        if (end - begin + 1) > std:
            print(end-begin+1, "std===> ", std, "bingo")
            return 1
        end += 1

    return -1

if __name__ == '__main__':
    input = input()
    print(input)
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)