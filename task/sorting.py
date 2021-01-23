# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    lt = l
    gt = r+1
    i = l+1
    print("sort=>", x, l, r)
    while i<gt:
        print('gt:', gt)
        if a[i]<x:
            lt += 1
            a[lt], a[i] = a[i], a[lt]
            i += 1
        elif a[i] >= x:
            gt -= 1
            a[gt], a[i] = a[i], a[gt]
        else:
            i += 1
    print("a==>", a, lt, gt)
    a[lt], a[l] = a[l], a[lt]        
    return lt, gt-1

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m-1)
    #should be n+1
    randomized_quick_sort(a, n+1, r)


if __name__ == '__main__':
    input = input()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')