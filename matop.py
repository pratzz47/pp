from operator import le
class MatOP:
    def addMat(self, arr, arr2):
        add = []
        for i in range(len(arr)):
            a = []
            for j in range(len(arr[i])):
                a.append(arr[i][j] + arr2[i][j])
                add.append(a)
        return add
    def subMat(self, arr, arr2):
        add = []
        for i in range(len(arr)):
            a = []
            for j in range(len(arr[i])):
                a.append(arr[i][j] - arr2[i][j])
                add.append(a)
        return add
    def mulMat(self, arr, arr2):
        result = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += arr[i][k]*arr2[k][j]
        return result

    def addString(self, str1, str2):
        return str1 + str2
