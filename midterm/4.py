"""
Hanoi Tower Problem
Input
3

Output
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3
"""

def hanoi_tower_count(n):
    return 2**n - 1

def hanoi_tower(n, source, aux, target):
    if n <= 1:
        print(source, target)
        return 0
    hanoi_tower(n-1, source, target, aux)
    print(source, target)
    hanoi_tower(n-1, aux, source, target)

n = int(input())  # 원판의 개수 
print(hanoi_tower_count(n))  # 총 이동 횟수; 2**n - 1
#hanoi_tower(n, "A", "B", "C")  # A:출발점, B:보조역할, C: 목적지
hanoi_tower(n, "1", "2", "3")