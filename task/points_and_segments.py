# Uses python3
import sys

def binary_search(p, arr, arrName, left, right):
    # print("p==>", p, left, right)
    # end case
    if right - left <= 1:        
        if arrName == 'start':
            if p < arr[left]:
                return left
            elif p < arr[right]:
                return right
            elif p >= arr[right]:
                return right + 1
        if arrName == 'end':
            if p <= arr[left]:
                return left
            elif p <= arr[right]:
                return right
            elif p > arr[right]:
                return right + 1       

    # normal
    mid = (left + right)//2
    # print("mid==>", mid)
    if arrName == 'start':
        if p < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if arrName == 'end':
        if p <= arr[mid]:
            right = mid - 1
        else:
            left = mid + 1 

    return binary_search(p, arr, arrName, left, right)
    

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    starts = sorted(starts)
    ends = sorted(ends)

    for index, p in enumerate(points):
        positionInStart = binary_search(p, starts, 'start', 0, len(starts)-1)
        # print("start==>", positionInStart)
        positionInEnd = binary_search(p, ends, 'end', 0, len(ends)-1)
        # print("end==>", positionInEnd)
        cnt[index] = positionInStart - positionInEnd

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = input()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')