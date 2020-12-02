# Symmetric Tree

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.
'''

# _______________________________________________Recursive_____________________________________________________________

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def isMirror(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val==t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        return isMirror(root, root)


# _______________________________________________Iterative_____________________________________________________________
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        queue = [root,root]
        
        while queue:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val!=t2.val:
                return False
            queue.extend([t1.left, t2.right, t1.right, t2.left])
                          
        return True
