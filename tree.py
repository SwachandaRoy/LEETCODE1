#Tree traversal
'''
preorder: DLR
inorder:LDR
postorder:LRD
use recursion'''

class Node:
    def _init_(self, v):
        self.left=None
        self.right=None
        self.data=v

def preorder(root):
    if root is None:
        return
    preorder(root.data)
    preorder(root.left)
    preorder(root.right)

'''further code required'''
