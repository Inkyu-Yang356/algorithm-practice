def rm_consecutive_dup(a):
    if not a:
        return []
    
    result = [a[0]]
    
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            result.append(a[i])
    
    return result

while True:
    line = input().split()
    n = int(line[0])
    if n == 0:
        break
    
    numbers = [int(x) for x in line[1:]]
    result = rm_consecutive_dup(numbers)
    
    print(' '.join(map(str, result)) + ' $')
