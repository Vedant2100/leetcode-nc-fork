class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        res = []
        indegree = defaultdict(int)
        q = deque()
        adj = defaultdict(list)

        for c, p in prerequisites:
            indegree[c] += 1
            adj[p].append(c)

        for c in range(numCourses): #cannot iterate over indegree nodes some course might not even be listed in prereq, ig theyll have 0 prereqs, so this is better
            if indegree[c] == 0:
                q.append(c)
    
        while q:
            c = q.popleft()
            res.append(c)
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []
          


#         # all valid answers - backtracking
#         # 
    
#         res = []
#         q = deque()
#         indegree = collections.defaultdict(int)

#         # topo sort  
#         adjlist = collections.defaultdict(list)
#         for c, p in prerequisites:
#             adjlist[p].append(c) # opposite direction
#             indegree[c] += 1

#         # queue init
#         for i in range(numCourses):
#             if indegree[i] == 0:
#                 q.append(i)

#         # Kahn
#         while q: # like BFS
#             node = q.popleft()
#             res.append(node)
#             for nei in adjlist[node]:
#                 indegree[nei] -= 1
#                 if indegree[nei] == 0:
#                     q.append(nei)

# #         If there is a cycle:
# # Some nodes will never reach indegree 0
# # So they will never enter the queue
# # So count < numCourses
# # So return False
# # To reduce indegree[0], we must first remove 1.
# # To reduce indegree[1], we must first remove 0.
# # So never reduced

#         return [] if len(res) != numCourses else res
