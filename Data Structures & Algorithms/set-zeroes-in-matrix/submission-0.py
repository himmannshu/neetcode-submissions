class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        
        def updateRows(i):
            for k in range(n):
                if matrix[i][k] != 0:
                    matrix[i][k] = -1
        
        def updateCols(j):
            for k in range(m):
                if matrix[k][j] != 0:
                    matrix[k][j] = -1

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == 0:
                    updateRows(i)
                    updateCols(j)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
        
        