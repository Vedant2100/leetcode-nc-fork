# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
res = []
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
Generic backtracking template.
"""     
        def dfs(node, curSum):
            if node is None:
                return
            curSum += node.val
            curPath.append(node.val)

            if node.left is None and node.right is None and curSum == targetSum:
                    result.append(curPath[:])

            dfs(node.left, curSum)
            dfs(node.right, curSum)
            curPath.pop()

        result = []
        curPath = []
        dfs(root, 0)
        
        return result

