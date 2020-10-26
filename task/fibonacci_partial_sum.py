def fibonacci_last_digital(n):
    n = n%60
    if n <= 1:
        return n

    previous = 0
    current  = 1
    
    # notice here range is 2 to n+3(finish at n+2)
    for _ in range(2, n+3):
        previous, current = current, (previous + current)%20

    return (current - 1)%10

def fibonacci_partial_sum_naive(from_, to):
    return (fibonacci_last_digital(to) + 10 - fibonacci_last_digital(from_-1))%10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))