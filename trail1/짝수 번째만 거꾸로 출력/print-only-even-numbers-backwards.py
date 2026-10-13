a = input()
b = len(a)
c = ""

for i in range(1, b, 2):
    c += a[i]

m = len(c)
for i in range(m-1 , -1, -1):
    print(c[i],sep="",end="")
