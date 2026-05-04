class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(indices):
            i, j = indices
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs((i + 1, j)) + dfs((i - 1, j)) + dfs((i, j + 1)) + dfs((i, j - 1))
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(dfs((i, j)), ans)
        
        return ans