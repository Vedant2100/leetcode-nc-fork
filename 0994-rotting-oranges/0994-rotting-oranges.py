class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        # multi source BFS
        fresh, time = 0, 0
        rows, cols = len(grid), len(grid[0])

        # get sources and fresh count
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        
        while fresh > 0 and q: # while is one wave
            for _ in range(len(q)): # missed 
                r, c = q.popleft() # did pop
                for dr, dc in directions:
                    rn, cn = r+ dr, c+ dc
                    if 0 <= rn < rows and 0 <= cn < cols and grid[rn][cn] == 1: # missed left side check 
                        grid[rn][cn] = 2
                        q.append((rn, cn))
                        fresh -= 1
            time += 1 # after a wave which is the while loop
        return time if fresh == 0 else -1
            
            