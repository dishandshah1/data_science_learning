def sort1(arr):
    for i in range(1,len(arr)):
        j = i

        while arr[j-1] > arr[j] and j>0:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                j=j-1
                

array1 = [5,6,2,3,1]
sort1(array1)
print(array1)

