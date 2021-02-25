# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash_func(s):
    multiplier = 67
    prime = 1000000007
    res = 0
    for i in reversed(s):
        res = (res*multiplier+ord(i))%prime
    return res

def get_occurrences(pattern, text):
    hp = hash_func(pattern)
    ht = hash_func(text[len(text) - len(pattern):])
    res = []
    multiplier = 67
    prime = 1000000007
    y = 1
    for i in range(len(pattern)):
        y = y*multiplier%prime
    for i in range(len(text) - len(pattern), -1, -1):
        if ht == hp:
            if pattern == text[i:i+len(pattern)]:
                res.append(i)
        if i > 0:
            ht = (ht*multiplier + ord(text[i-1]) - ord(text[i+len(pattern)-1])*y) % prime
    return reversed(res)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))