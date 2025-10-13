n = int(input())

def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

li = []
for i in range(n): li.append(input())

#print('ABBA:', isPalindrome('ABBA'))
#print('ABC:', isPalindrome('ABC'))

for s in li:
    count = 0
    print(isPalindrome(s), count)