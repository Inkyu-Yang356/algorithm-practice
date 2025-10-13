n = int(input())

def hanoi(n):
    print(2**n - 1)
    def move(n, a, b, c):
        if n == 1:
            print(a, c)
            return
        move(n-1, a, c, b)
        print(a, c)
        move(n-1, b, a, c)
    move(n, 1, 2, 3)
hanoi(n)