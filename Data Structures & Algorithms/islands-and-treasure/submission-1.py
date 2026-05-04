class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        LAND = pow(2,31) - 1
        r = len(grid)
        c = len(grid[0]) 

        def bfs(i, j):
            q = deque()
            q.append((i, j, 0))
            visited = set()
            while q:
                x, y, dist = q.popleft()
                
                if grid[x][y] != 0 and grid[x][y] != -1:
                    grid[x][y] = min(dist, grid[x][y])
                visited.add((x, y))
                directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

                for xi, yi in directions:
                    _x = x + xi
                    _y = y + yi
                    if (_x, _y) not in visited and _x >= 0 and _x < r and _y >= 0 and _y < c and grid[_x][_y] != -1:
                        q.append((_x, _y, dist + 1))

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    bfs(i, j) # reverse engineer