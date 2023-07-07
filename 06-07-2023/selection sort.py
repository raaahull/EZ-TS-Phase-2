arr=[45,22,33,41,56,75]

for i in range(len(arr)):
    min_ind=i
    for j in range(i+1,len(arr)):
        if arr[min_ind]>arr[j]:
            min_ind=j
    arr[i], arr[min_ind]=arr[min_ind],arr[j]
print(arr)
