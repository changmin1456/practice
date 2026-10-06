n, m = input().split()
i = len(n)
j = len(m)

if i > j :
    print(n, i)
elif  i < j : 
    print(m, j)
else :
    print("same")