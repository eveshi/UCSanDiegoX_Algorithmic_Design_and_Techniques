# Sum of nth Fibonacci series = F(n+2) -1

def fibonacci_sum_naive(n):
    n = n%60
    if n <= 1:
        return n

    previous = 0
    current  = 1
    
    # notice here range is 2 to n+3(finish at n+2)
    for _ in range(2, n+3):
        previous, current = current, (previous + current)%20

    return (current - 1)%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_naive(n))