import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        print("matrix after taking transpose",matrix)
#         now lets do the swap about Axis
        x=math.floor(len(matrix)/2)
        for i in range(len(matrix)):
            for j in range(x):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][len(matrix)-1-j]
                matrix[i][len(matrix)-1-j]=temp
        print("matrix after doing swap around y axis",matrix)
        