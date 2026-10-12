n = int(input())
sum = 0 
num = 0 


for i in range(n):
    m = input()
    sum += len(m)
    if m[0] == 'a':
       num += 1

print(sum, num)
