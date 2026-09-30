n, m = map(int, input().split())

num  = 1
arr = [[0]* m for _ in range(n)]

for k in range(n+m-1):
    for i in range(n):
        j = k - i

        if 0 <= j < m :
            arr [i][j] = num
            num += 1

for i in range(n):
    print(*arr[i])
