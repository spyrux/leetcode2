# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    #return the length of a leg
    def dfs(self, root:Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left = 0
        right = 0
        if root.right:
            right = 1+self.dfs(root.right)
        if root.left:
            left = 1+self.dfs(root.left)

        self.diameter = max(self.diameter, left+right)

        return max(left,right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #for each node get length of left and length of right and take the max
        self.dfs(root)
        return self.diameter




        