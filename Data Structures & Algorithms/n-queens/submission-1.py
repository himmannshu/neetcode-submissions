class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = set()

        def is_valid(x, y, board):
            # check column
            for i in range(n):
                if board[i][y] == 'Q':
                    return False
            
            # check upper left diagonal
            xi, yi = x - 1, y - 1
            while xi >= 0 and yi >= 0:
                if board[xi][yi] == 'Q':
                    return False
                xi -= 1
                yi -= 1
            
            # check upper right diagonal
            xi, yi = x - 1, y + 1
            while xi >= 0 and yi < n:
                if board[xi][yi] == 'Q':
                    return False
                xi -= 1
                yi += 1
            
            return True

        def placements(x, ni, board):
            if ni == 0:
                ans.add(tuple([''.join(row) for row in board]))
                return
            for i in range(n):
                if is_valid(x, i, board):
                    board[x][i] = 'Q'
                    placements(x + 1, ni - 1, board)
                    board[x][i] = '.'
        
        placements(0, n, [['.' for _ in range(n)] for _ in range(n)])
        
        ans_format = []
        for board in ans:
            ans_format.append(list(board))
        return ans_format
            