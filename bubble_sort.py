def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1): # for every iteration it starts from the first element of the array and compares adjacent element
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr
arr=list(map(int,input().split()))
print(bubble_sort(arr))