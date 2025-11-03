"""
Sum of Integers from 1 to N

Input
10

Output
55
"""

def sum_n(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

n = int(input())  # 입력받은 정수를 1부터 총합
print(sum_n(n))