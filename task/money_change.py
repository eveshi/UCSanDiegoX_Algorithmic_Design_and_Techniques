import sys

def get_change(m):
    #write your code here
    tens = m//10
    rest = m%10
    fives = rest//5
    rest = rest%5
    return tens+fives+rest

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))