n = input()
m = input()

num = 0

for c in range(len(n)):
    if n[c] == m:
        num += 1

print(num)