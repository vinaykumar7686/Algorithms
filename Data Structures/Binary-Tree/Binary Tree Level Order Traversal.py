# Binary Tree Level Order Traversal

'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        
        ans = dict()
        
        def subfunc(lvl, root):
            if not root:
                return
            # print(ans)
            if lvl in ans:
                ans[lvl].append(root.val)
            else:
                ans[lvl] = [root.val]
                
            subfunc(lvl+1, root.left)
            subfunc(lvl+1,root.right)
            
        subfunc(0, root)
        
        
        return list(ans.values())
