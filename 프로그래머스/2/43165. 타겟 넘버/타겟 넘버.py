from collections import deque

def solution(li, target):
    qu = deque([(0, 0)])
    count = 0
    while qu:
        idx, total = qu.popleft()
        if idx == len(li):
            if total == target:
                count += 1
        else:
            qu.append((idx + 1, total + li[idx]))
            qu.append((idx + 1, total - li[idx]))
    return count