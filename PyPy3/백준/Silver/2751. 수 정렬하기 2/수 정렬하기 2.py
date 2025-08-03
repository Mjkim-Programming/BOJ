n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

# Changed to internal sorting function because of timeout   
#for i in range(len(arr)):
#    for j in range(len(arr) - 1):
#        if(arr[j] > arr[j+1]):
#            temp = arr[j]
#            arr[j] = arr[j+1]
#            arr[j+1] = temp

arr.sort()
 
for i in arr:
    print(i) 