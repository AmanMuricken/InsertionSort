def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

arr=[4,1,30,25,44,22,21,15,50]
insertionSort(arr)
print(arr)

    