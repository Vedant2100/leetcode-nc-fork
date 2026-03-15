class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # rows, cols = len(grid), len(grid[0])
        # minDist = float('inf')
        # onpath = set()
        # minDict = {}
        # if grid[0][0] == 1:
        #     return -1
        # def dfs(r, c):
        #     if not (0 <= r < rows and 0 <= c < cols):
        #         return float('inf')
        #     if grid[r][c] == 1:
        #         return float('inf')
        #     if (r, c) in minDict:
        #         return minDict[(r,c)]
        #     if (r, c) in onpath:
        #         return float('inf')
        #     if r == rows - 1 and c == cols - 1 and grid[r][c] == 0:
        #         minDict[(r,c)] = 1
        #         return 1
        #     elif r == rows - 1 and c == cols - 1 and grid[r][c] != 0:
        #         return float('inf')
        #     onpath.add((r, c))
        #     minDist = float('inf')
        #     if 0 <= r < rows and 0<= c < cols and grid[r][c] == 0:
        #         directions = [(0,1), (1,0), (0,-1), (-1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1)]
        #         best = float('inf')
        #         for dr, dc in directions:
        #             best = min(best, dfs(r+dr, c+dc))
        #         minDict[(r, c)] = 1 + best
        #         onpath.remove((r, c))
        #         return 1 + best
        #     onpath.remove((r, c)) 
        #     # minDict[(r,c)] = best
        #     return float('inf')
        # ans = dfs(0,0)
        # return -1 if ans == float('inf') else ans
        if grid[0][0] != 0:
            return -1 
        q = deque()
        q.append((0,0))
        rows, cols = len(grid), len(grid[0])
        waves = 1
        visited = set() # if unused causes MLE
        while q:    
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == rows - 1 and c == cols- 1:
                    return waves
                for dr, dc in [(0,1), (1,0), (0,-1), (-1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1)]:
                    if 0 <= r+dr < rows and 0 <= c+dc < cols and grid[r+dr][c+dc] == 0 and (r+dr, c+dc) not in visited:
                        q.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
            waves += 1 
        return -1
        
