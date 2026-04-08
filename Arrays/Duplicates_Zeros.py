# Two pointer Approach

#arr = [1,0,2,3,0,4,5,0] o/p = [1,0,0,2,3,0,0,4]

arr = [1,0,2,3,0,4,5,0]
n=len(arr)
zero=arr.count(0)
i=n-1
j=n+zero-1
while i<j:
    if j<n:
        arr[j]=arr[i]
    if arr[i]==0:
        j-=1
        if j<n:
            arr[j]=0
    i-=1
    j-=1
print(arr)
