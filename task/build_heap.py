def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for position in range(len(data)//2, 0, -1):
        curr = position - 1 
        while curr < len(data):
            # print("curr:", curr, data[curr])
            left = 2*curr + 1
            right = 2*curr + 2
            min_index = curr
            if (left<len(data)) and (data[min_index] > data[left]):
                min_index = left
            if (right<len(data)) and (data[min_index] > data[right]):
                min_index = right
            
            if min_index != curr:
                swaps.append((curr, min_index))
                data[curr], data[min_index] = data[min_index], data[curr]
                curr = min_index
                print(data)
            else:
                # print("break==>", data)
                break
    
    # print(data)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()