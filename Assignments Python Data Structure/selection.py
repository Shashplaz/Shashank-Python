arr=[1,6,3,5,4,7]
i=0
while i<5:
    mind=arr[i]
    pos=i
    j=i
    while j<6:
        if arr[j]<mind:
            mind=arr[j]
            pos=j
        j=j+1

    t=arr[i]
    arr[i]=mind
    arr[pos]=t
    i=i+1
print(arr)