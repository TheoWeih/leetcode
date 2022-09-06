# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


# Recursion (DFS) approach
# Also possible would be BFS with a queue structure

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if root is None: 
                return depth
            return max(dfs(root.left, depth+1), dfs(root.right, depth+1))
        
        return dfs(root, 0)
        