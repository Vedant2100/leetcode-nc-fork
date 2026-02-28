class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True
            if not 0<= r< rows or not 0 <= c< cols or board[r][c] != word[index]:
                return False
            temp, board[r][c] = board[r][c], '#' # useful for avoiding finding "ABAC" using [[A, B, C]]
            found = dfs(r +1, c, index + 1) or dfs(r, c+1, index + 1) or dfs(r-1, c, index + 1) or dfs(r, c-1, index + 1)
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False
        
        
        
        
        
        
        
        
        
        
        # DFS WITH AN OBJECTIVE
        # rows, cols = len(board), len(board[0])

        # def dfs(r, c, index):
        #     if index == len(word):
        #         return True
        #     if r < 0 or c < 0 or r >= rows or c >= cols:
        #         return False
        #     if board[r][c] != word[index]:
        #         return False

        #     # mark visited
        #     temp = board[r][c]
        #     board[r][c] = '#'

        #     # explore neighbors
        #     found = (
        #         dfs(r+1, c, index+1) or
        #         dfs(r-1, c, index+1) or
        #         dfs(r, c+1, index+1) or
        #         dfs(r, c-1, index+1)
        #     )

        #     # backtrack
        #     board[r][c] = temp
        #     return found

        # for r in range(rows):
        #     for c in range(cols):
        #         if dfs(r, c, 0):
        #             return True

        # return False

        # DFS WITH AN OBJECTIVE
        