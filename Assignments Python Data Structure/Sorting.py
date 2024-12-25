#          j
#  1 8 4 5 9
#          i
#                 numb       i     mind    pos    j    t
#                  5         0       1      0     1    1
#                            1       8      1     2    8
#                            2       4      2     3    4
#                            3       5      3     4    5
#                            5              5     5
arr=[1,8,4,5,9]
i=0

numb=len(arr)
while i<(numb-1):
    mind=arr[i]
    pos=i
    j=i
    while j<numb:
        if arr[j]<mind:
            mind=arr[j]
            pos=j
        j=j+1
    t=arr[i]
    arr[i]=mind
    arr[pos]=t
    i=i+1
print(arr)