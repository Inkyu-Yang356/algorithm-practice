memo = {}

def fibonacci_count(n):
    if n in memo:
        return memo[n]
    
    if n == 0:
        memo[n] = (1, 0)  # (0의 개수, 1의 개수)
    elif n == 1:
        memo[n] = (0, 1)  # (0의 개수, 1의 개수)
    else:
        count_0_prev, count_1_prev = fibonacci_count(n-1)
        count_0_prev2, count_1_prev2 = fibonacci_count(n-2)
        memo[n] = (count_0_prev + count_0_prev2, count_1_prev + count_1_prev2)
    
    return memo[n]

n = int(input())
for _ in range(n):
    f = int(input())
    count_0, count_1 = fibonacci_count(f)
    print(count_0, count_1)
