A = input()
count = 1
result = ""

for i in range(len(A) - 1):
    if A[i] == A[i+1]:
        count += 1
    else:
        result += A[i] + str(count)
        count = 1

result += A[-1] + str(count)

print(len(result))
print(result)