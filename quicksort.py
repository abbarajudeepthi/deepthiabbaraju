def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quicksort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)
array=[2, 6, 62,26, 72, 8989, -2, -1]
size=len(array)
quicksort(array,0,size-1)
print(array)