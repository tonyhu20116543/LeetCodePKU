# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        memo = [[None] * (n + 1) for _ in range(n + 1)]  # store immediate child trees [start:end]
        
        def helper(start, end):
            if start > end:
                return [None]
            if memo[start][end] is not None:
                return memo[start][end]
            
            res = []
            for i in range(start, end + 1):
                left = helper(start, i - 1)
                right = helper(i + 1, end)
                
                for p in left:
                    for q in right:
                        root = TreeNode(i)  # create root and add left&right child tree
                        root.left = p
                        root.right = q
                        res.append(root)
            
            memo[start][end] = res
            return res
        
        return helper(1, n) if n != 0 else []
