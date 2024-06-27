# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node=root
        if not root:
            return 0
        dq=deque([root])
        lvl=0
        while dq:
            for i in range(len(dq)):
                node=dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            lvl+=1
        return lvl
            

        
