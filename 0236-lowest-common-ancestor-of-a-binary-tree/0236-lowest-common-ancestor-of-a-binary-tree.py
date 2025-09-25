# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #if root is null return none
        if not root:
            return None
        #dfs left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # if left has either p or q and right has either p or q then root is the lowest
        # if root is p or q then root is lowest
        if (left and right) or (root in [p,q]):
            return root

        return left or right
        

