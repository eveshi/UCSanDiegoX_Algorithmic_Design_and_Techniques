import sys
import functools

def custom_sort(str1, str2):
    if(str1+str2 > str2+str1):
        return 1
    return -1


def largest_number(a):
    #write your code here
    astring = [str(i) for i in a]
    print(astring)
    astring.sort(key=functools.cmp_to_key(custom_sort), reverse=True)
    print(astring)

    res = ""
    for x in astring:
        res += x
    return res

if __name__ == '__main__':
    input = input()
    data = input.split()
    a = data[1:]
    print(largest_number(a))