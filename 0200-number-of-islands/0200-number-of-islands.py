class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        visited = set()

        def dfs(r, c):
            if (r,c) in visited:
                return 0
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
                visited.add((r, c))
                dfs(r, c-1)
                dfs(r, c+1) 
                dfs(r-1, c)
                dfs(r+1, c)
                return 1
            else:
                return 0
        
        for r in range(rows):
            for c in range(cols):
                count += dfs(r,c)
        return count
