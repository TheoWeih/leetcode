# https://leetcode.com/problems/invert-binary-tree/
# 226. Invert Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive Solution
#         if root:
#             root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

#             return root

        # Iterative Solution
        if root:
            queue = deque()
            queue.append(root)
            
            while queue:
                currentNode = queue.popleft()
                currentNode.left, currentNode.right = currentNode.right, currentNode.left
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return root
            