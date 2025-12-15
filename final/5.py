from collections import deque

def target_number(arr, y):
    qu = deque([(0,0)])  # idx:, total
    count = 0  # how many it matches in the final index

    while qu:
        idx, total = qu.popleft()
        if idx == len(arr):  # Calculation Index
            if total == y:
                count += 1
        else:  # Both Plus, Minus
            qu.append((idx+1, total+arr[idx]))
            qu.append((idx+1, total-arr[idx]))
    return count

numbers = list(map(int, input().split()))
target = int(input())

#numbers = [1, 1, 1, 1, 1]
#target = 3

#numbers = [4, 1, 2, 1]
#target = 4

cnt = target_number(numbers, target)
print(cnt)