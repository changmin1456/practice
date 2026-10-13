arr = input()
n = int(input())

for i in range(min(n, len(arr))):
    print(arr[len(arr) - 1 - i], end="")