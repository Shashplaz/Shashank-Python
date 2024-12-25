arr=[6,5,2,4,8]
i=0
while i<4:
    j=0
    while j < 4:
        if arr[j] < arr[j+1]:
            r=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=r
        j=j+1
    i=i+1
print(arr)