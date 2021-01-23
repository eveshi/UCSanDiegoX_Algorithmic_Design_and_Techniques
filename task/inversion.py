# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    # print(a, b, left, right)
    if right == left:
        return [[a[left]], number_of_inversions]
    ave = (left + right) // 2
    # print(a, b, left, right, ave)
    left = get_number_of_inversions(a, b, left, ave)
    right = get_number_of_inversions(a, b, ave+1, right)
    number_of_inversions += left[1]
    number_of_inversions += right[1]
    #write your code here
    rightPart = right[0]
    leftPart = left[0]
    newArray = []
    # print("before ==>", leftPart, rightPart)
    while (len(rightPart) != 0) & (len(leftPart) != 0):
        # print("compare ==>", leftPart[0], rightPart[0], leftPart[0] <= rightPart[0])
        if leftPart[0] <= rightPart[0]:
            newArray.append(leftPart[0])
            leftPart.pop(0)
        else:
            newArray.append(rightPart[0])
            rightPart.pop(0)
            number_of_inversions += len(leftPart)
    newArray.extend(leftPart)
    newArray.extend(rightPart)
    # print(newArray, number_of_inversions)
    return [newArray, number_of_inversions]

if __name__ == '__main__':
    input = input()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1)[1])