class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0

        def dfs(indices, n, m):
            i, j = indices
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == "0":
                return
            # 4 possible directions
            grid[i][j] = "0"
            dfs((i + 1, j), n, m)
            dfs((i - 1, j), n, m)
            dfs((i, j + 1), n, m)
            dfs((i, j - 1), n, m)    
               
        for k in range(n):
            for l in range(m):
                if grid[k][l] == "1":
                    ans += 1
                    dfs((k, l), n, m)
                                 
        return ans