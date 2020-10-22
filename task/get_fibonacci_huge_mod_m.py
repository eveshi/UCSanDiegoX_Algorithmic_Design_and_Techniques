# pls search for pisano_period for more details
def find_pisano_period(n, m):
    previous = 0
    current  = 1

# range is m*m here
    for i in range(m*m):
        previous, current = current, (previous + current)%m

        if(previous==0 and current==1):
            return i+1

def get_fibonacci_huge_naive(n, m):
    period = find_pisano_period(n, m)
    n = n%period

    # notice that should get new n first, then check if n <= 1
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%m

    return current

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(get_fibonacci_huge_naive(a, b))