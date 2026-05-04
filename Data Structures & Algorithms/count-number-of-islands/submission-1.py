class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 0 < len(grid), len(grid[i]) 
        n = len(grid)
        m = len(grid[0])
        ans = 0
        
        def dfs(matrix, i, j, n, m):
            if i < 0 or j < 0 or i >= n or j >= m or matrix[i][j] == "0":
                return
            
            matrix[i][j] = "0"

            dfs(matrix, i - 1, j, n, m)
            dfs(matrix, i + 1, j, n, m)
            dfs(matrix, i, j - 1, n, m)
            dfs(matrix, i, j + 1, n, m)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(grid, i, j, n, m)
                    ans += 1
        
        return ans
        