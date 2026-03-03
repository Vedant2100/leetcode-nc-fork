"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # instead use a dict with the nodes themselves as keys. a lot of meta thinking 
        if node is None:
            return None
        clones = {}
        q = deque([node])

        while q:
            curr = q.popleft()
            if curr not in clones:
                clones[curr] = Node(curr.val)
            for nei in curr.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    q.append(nei)
                clones[curr].neighbors.append(clones[nei]) 
        return clones[node]

        # below wont work coz duplicate nodes - dict storage wont work
        # if node is None:
        #     return None
        # q = deque([node])
        # visited = set()
        # adj = defaultdict(list)
        # visited.add(node)

        # while q:
        #     curr = q.popleft()
        #     adj[curr.val] = [nei.val for nei in curr.neighbors]
        #     for nei in curr.neighbors:
        #         if nei not in visited:
        #             q.append(nei)
        #             visited.add(nei)
        
        # # stage 1 graph
        # clones = {} # a dict of nodes to organise

        # for node in list(adj.keys()):
        #     clones[node] = Node(node)
        # # Stage 2, why coz we need new stuff
        # for node, neighbors in adj.items():
        #     clones[node].neighbors = [clones[i] for i in neighbors]

        # return clones[node]


        # # Adj list construct 
        # adjlist = Collections.defaultdict(list)
        # q = deque()
        # # q.append(Node(node.val, node.neighbors)) # doesnt accomplish shit
        # q.append(node) #might as well
        # # one case where we need to track visited i n BFS is while constructoing from BFS
        # visited = set()
        # while q:
        #     curr = q.popleft()
        #     # adjlist[curr.val] = curr.neighbors[:] # lists aere mutable
        #     adjlist[curr.val] = [n.val for n in curr.neighbors]
        #     visited.add(curr)
        #     for nei in curr.neighbors:
        #         if nei not in visited:
        #             q.append(nei)
        # clones = {}
        # for value, neighborlist in adjlist:
        #     clones[value] = Node(value, neighborlist)


        # # adjlist 
        # if not node:
        #     return None

        # q = deque()
        # newhead = Node(node.val, node.neighbors)
        # q.append(newhead)

        # while q:
        #     curr = q.popleft()
        #     for nei in curr.neighbors:
        #         new = Node(nei.val, nei.neighbors) # THESE ARE STILL OLD REFERENCES

        #         del nei
        #         q.append(new)
        #     del curr 
        
        # return newhead

 # You are getting memory limit exceeded because this is not actually cloning the graph. It is repeatedly recreating nodes while still pointing to the original neighbor lists, and you never track what has already been copied.


            
        
        


            

        