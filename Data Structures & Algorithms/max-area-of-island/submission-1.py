class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(grid, i, j, n, m):
            
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0

            return 1 + dfs(grid, i + 1, j, n, m) + dfs(grid, i - 1, j, n, m) + dfs(grid, i, j + 1, n, m) + dfs(grid, i, j - 1, n, m)

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(grid, i, j, n, m))
        
        return ans