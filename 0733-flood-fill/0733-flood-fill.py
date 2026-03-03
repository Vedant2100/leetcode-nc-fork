class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        original = image[sr][sc]
        if color == original:
            return image
        rows, cols = len(image), len(image[0])
        def dfs(r, c):
            if image[r][c] == original:
                image[r][c] = color   
                directions  = [[0,1], [1,0], [0,-1], [-1,0]]
                for dr, dc in directions:
                    r_n, c_n = r+dr, c+dc
                    if 0 <= r_n < rows and 0 <= c_n < cols and image[r_n][c_n] == original:
                        dfs(r_n, c_n)

            return
        dfs(sr, sc)
        return image


