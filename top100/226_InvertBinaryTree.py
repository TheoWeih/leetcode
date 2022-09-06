# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # a, b = b, a , allows for swapping in the same line
            # where otherwise you would need to use a temp
            # e.g.
            # temp = a
            # a = b
            # b = temp
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

            return root