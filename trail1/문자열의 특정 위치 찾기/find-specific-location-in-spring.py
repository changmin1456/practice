n, m = input().split()
count = 0

for i in range(len(n)):
    if m == n[i]:
        print(count)
        break
    else:
        count += 1

if count == len(n):
    print("No")