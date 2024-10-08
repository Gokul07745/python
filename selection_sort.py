def selection_sort(arr):
    for i in range(len(arr)):
        min =i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
                       
print(selection_sort([2,9,4,1,8,0]))