# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        arr1=[]
        arr2=[]
        def dfs(root, arr):
            if not root:
                return
            if not root.left and not root.right:
                arr.append(root.val)
                return
            dfs(root.left, arr)
            dfs(root.right, arr)
        
        dfs(root1, arr1)
        dfs(root2, arr2)
        return arr1==arr2
        
        
