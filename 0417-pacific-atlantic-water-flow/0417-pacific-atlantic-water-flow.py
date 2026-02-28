class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #DFS
        rows, cols = len(heights), len(heights[0])
        res = []  
        visitedAtlantic, visitedPacific = set(), set()
        def dfsPacific(r, c, nei):
            # if not 0 <= r< rows or not 0 <= c< cols:
            #     return False
            # if (r == rows-1 or c == cols-1):
            #     return True
            if (r, c) in visitedPacific:
                # print(f"{(r,c)} already visited and confirmed")
                return 
            visitedPacific.add((r, c))
            # print(f"Starting at {(r,c)}")
            for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                # print(r+dr, c+dc)
                if 0 <= r+dr< rows and 0 <= c+dc< cols and heights[r+dr][c+dc] >= heights[r][c] and (r+dr, c+dc) != nei: 
                    # if (r+dr, c+dc) == nei or not dfsAtlantic(r+dr, c+dc, (r,c)):
                    #     continue
                    # else:
                        # print(f"foudn True Pacific for {(r+dr,c+dc)} called by {(r,c)}")
                        dfsPacific(r+dr, c+dc, nei)
            return

        def dfsAtlantic(r, c, nei):
            # if not 0 <= r< rows or not 0 <= c< cols:
            #     return False
            # if (r == rows-1 or c == cols-1):
            #     return True
            if (r, c) in visitedAtlantic:
                # print(f"{(r,c)} already visited and confirmed")
                return 
            visitedAtlantic.add((r, c))
            # print(f"Starting at {(r,c)}")
            for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                # print(r+dr, c+dc)
                if 0 <= r+dr< rows and 0 <= c+dc< cols and heights[r+dr][c+dc] >= heights[r][c] and (r+dr, c+dc) != nei: 
                    # if (r+dr, c+dc) == nei or not dfsAtlantic(r+dr, c+dc, (r,c)):
                    #     continue
                    # else:
                        # print(f"foudn True Atlantic for {(r+dr,c+dc)} called by {(r,c)}")
                        dfsAtlantic(r+dr, c+dc, nei)
            
            return
            # print(f"found nothing for {(r,c)}")

        # dfs on every cell doesnt eork tle
        # for r in range(rows):
        #     for c in range(cols):
        #         if (r,c) in visitedAtlantic:
        #             continue
        #         dfsAtlantic(r,c, None)
        #         if (r,c)  in visitedPacific:
        #             continue
        #         dfsPacific(r,c, None)
        # r = [0,1,2,3,4] , c = 0
        # pacific connected cells
        for r in range(rows):
            c = 0
            if (r,c) in visitedPacific:
                continue
            dfsPacific(r,c, None)
        for c in range(cols):
            r = 0
            if (r,c) in visitedPacific:
                continue
            dfsPacific(r,c, None)
        for r in range(rows):
            c = cols-1
            if (r,c) in visitedAtlantic:
                continue
            dfsAtlantic(r,c, None)
        for c in range(cols):
            r = rows-1
            if (r,c) in visitedAtlantic:
                continue
            dfsAtlantic(r,c, None)
        
                    
        # # r,c = 2,  2
        # print(dfsAtlantic(1, 4))
        # print(visitedAtlantic)
        # print(dfsPacific(1, 4))
        return list(visitedAtlantic.intersection(visitedPacific))