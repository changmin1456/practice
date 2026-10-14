n = input()
ecount = 0
dcount = 0
for i in range(len(n)-1):
    if n[i] == "e" and n[i+1] == "e":
        ecount += 1
    elif n[i] == "e" and n[i+1] == "b":
        dcount += 1

print(ecount, dcount)