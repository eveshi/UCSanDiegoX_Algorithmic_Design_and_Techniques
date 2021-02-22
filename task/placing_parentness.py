import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    curr = 0
    ns = []
    ops = []

    for i in dataset:
        if i in ['+', '-', '*']:
            ns.append(curr)
            ops.append(i)
            curr = 0
        elif i != ' ':
            curr = curr*10 + int(i)
    ns.append(curr)
    min_table = [[0 for _ in range(len(ns))] for _ in range(len(ns))]
    max_table = [[0 for _ in range(len(ns))] for _ in range(len(ns))]
    for j in range(len(ns)):
        for i in range(len(ns)):
            if j == 0:
                min_table[i][i+j] = ns[i]
                max_table[i][i+j] = ns[i]
            elif i+j < len(ns):
                max_val = -math.inf
                min_val = math.inf
                for z in range(j):
                    if ops[i+z] == "+":
                        max_val = max(max_val, max_table[i][i+z] + max_table[i+z+1][i+j])
                        min_val = min(min_val, min_table[i][i+z] + min_table[i+z+1][i+j])
                    elif ops[i+z] == "-":
                        max_val = max(max_val, max_table[i][i+z] - min_table[i+z+1][i+j])
                        min_val = min(min_val, min_table[i][i+z] - max_table[i+z+1][i+j])
                    elif ops[i+z] == "*":
                        max_val = max(max_val, max_table[i][i+z] * max_table[i+z+1][i+j], min_table[i][i+z] * min_table[i+z+1][i+j])
                        min_val = min(min_val, max_table[i][i+z] * max_table[i+z+1][i+j], min_table[i][i+z] * min_table[i+z+1][i+j])
                min_table[i][i+j] = min_val
                max_table[i][i+j] = max_val
                    
    return max_table[0][len(ns)-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))