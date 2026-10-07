arr = ["apple", "banana", "grape", "blueberry", 'orange']

n = input()
num = 0

for i in range(5):
    if arr[i][2] == n or arr[i][3] == n:
        print(arr[i])
        num +=1
    
print(num)