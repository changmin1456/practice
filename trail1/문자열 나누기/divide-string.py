n = int(input())
a = "".join(input().split())

for i in range(len(a)):
    print(a[i], end="")

    if (i + 1) % 5 == 0:
        print()
    