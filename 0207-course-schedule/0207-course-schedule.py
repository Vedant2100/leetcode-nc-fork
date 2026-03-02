class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = collections.defaultdict(list)
        for course, prereq in prerequisites:
            adjlist[course].append(prereq)

        courses = set(adjlist.keys())
        visited = set()
        onpath= set() # for cycle detection

        def cycle(node):
            if node in visited:
                return False
            if node in onpath:
                # print("hi")
                return True
            onpath.add(node)
            for prereq in adjlist[node]:
                # print(f"checking for {prereq} for {node}")
                if cycle(prereq):
                    return True
            onpath.remove(node)
            visited.add(node)
            return False
        cycleExists = False
        for course in courses:
            if cycle(course):
                cycleExists = True
        return not cycleExists




        # #graph from course ot preq
        # adj = collections.defaultdict(list)
        # for c, p in prerequisites:
        #     adj[c].append(p)
        # visited = set() #efficeincy
        # onpath = set()
        # def dfs(c):
        #     if c in visited:
        #         return True # no cycle, just skip
        #     if c in onpath:
        #         return False # cycle i
        #     onpath.add(c)
        #     for nei in adj[c]:
        #         if not dfs(nei):
        #             return False
        #     onpath.remove(c)
        #     visited.add(c) # at the end 
        #     return True
        # for c in range(numCourses):
        #     if dfs(c) is False:
        #         return False
        # return True





        # # cycle detection problem in graph? 
        # # DFS
        # # first adjacency list from 
        # adj = collections.defaultdict(list)
        # for c, p in prerequisites:
        #     adj[c].append(p)
        # visited = set()
        # onpath = []
        # def dfs(node):
        #     if node in visited: # no extra same computation
        #         return True
        #     if node in onpath: # cycle
        #         return False
        #     onpath.append(node)
        #     for nb in adj[node]:
        #         if dfs(nb) is False:
        #             return False
        #     onpath.remove(node)
        #     visited.add(node)
        #     return True
        
        # for c in range(numCourses):
        #     if dfs(c) is False:
        #         return False
        # return True
            

    