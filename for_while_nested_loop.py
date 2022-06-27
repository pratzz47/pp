def bubbleSort(arr, i):
     while i < len(arr):
         for j in range(0, len(arr)-i-1):
             if arr[j] > arr[j+1]:
                 temp = arr[j]
                 arr[j]= arr[j+1]
                 arr[j+1]=temp
         i = i + 1
     print("Sorted Array elements are : ", arr)

 #arr = {10,20,30,40,50}
arr = [10,20,40,2,6,1,12]
print("Before Sorting Array : ", arr)
bubbleSort(arr, 1)
