n = int(input())

m = []

for i in range(n):
    m.append(input())

s = input()

num = 0
sum = 0

for i in range(n):
    if m[i][0] == s:
        num += 1
        sum += len(m[i])

print(num, f"{sum / num:.2f}")