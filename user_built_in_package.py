from Python_Practicals import matop
arr = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = [[10,20,30],[40,50,60],[70,80,90]]
mat = matop.MatOP()
print("Addition is:",mat.addMat(arr,arr2=arr2))
print("Subtraction is:",mat.subMat(arr,arr2=arr2))
print("Multiplication is:",mat.mulMat(arr,arr2=arr2))
