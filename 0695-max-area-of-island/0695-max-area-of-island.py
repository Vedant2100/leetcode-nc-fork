class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(r, c):
            if (r,c) in visited:
                return 0
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                visited.add((r,c))
                return 1 + dfs(r, c-1)+ dfs(r, c+1) + dfs(r+1, c) + dfs(r-1, c)
            else:
                return 0
        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, dfs(r,c))
        return maxArea
