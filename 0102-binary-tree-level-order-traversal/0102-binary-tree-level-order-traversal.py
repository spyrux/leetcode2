# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #store curr level's nodes in an array
        #store next level's nodes in an array and add to curr when curr is done
        curr = [root]
        traversal = []
        if not root:
            return traversal
        while curr:
            currLength = len(curr)
            currLevel = []
            while currLength > 0:
                node = curr.pop(0)
                if node:
                    if node.left:
                        curr.append(node.left)
                    if node.right:
                        curr.append(node.right)
                    currLevel.append(node.val)
                    currLength -= 1
            traversal.append(currLevel)

        return traversal




