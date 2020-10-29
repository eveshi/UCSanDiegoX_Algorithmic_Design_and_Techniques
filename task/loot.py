import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    unitsValue = [(v/w, w, v) for w, v in zip(weights, values)]
    unitsValue = sorted(unitsValue, key=lambda  x: x[0], reverse=True)
    for item in unitsValue:
        if capacity == 0:
            return value
        
        if item[1] > capacity:
            value += item[0]*capacity
            capacity = 0
        else:
            value += item[2]
            capacity -= item[1]

    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
