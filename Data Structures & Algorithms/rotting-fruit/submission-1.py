class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        k = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            x, y, _k = q.popleft()
            visited.add((x, y))
            grid[x][y] = 2
            for dx, dy in directions:
                x_ = x + dx
                y_ = y + dy
                if x_ < 0 or x_ >= m or y_ < 0 or y_ >= n or (x_, y_) in visited or grid[x_][y_] != 1:
                    continue
                q.append((x + dx, y + dy, _k + 1))
            k = max(k, _k)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return k
                
