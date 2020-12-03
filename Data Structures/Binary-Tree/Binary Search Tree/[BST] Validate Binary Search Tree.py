# Validate Binary Search Tree

'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
        
        
    def isValidBST(self, root: TreeNode) -> bool:
        
        def func(root, l, r):
            
            if root:
                
                if root.val<=l or root.val>=r:
                    self.ans = False
                    return
                
                func(root.left, l, root.val)
                func(root.right, root.val, r)
                
                
        func(root, float("-inf"), float("inf"))
        return self.ans
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def __init__(self):
        self.nums = []
    def isValidBST(self, root: TreeNode) -> bool:
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            self.nums.append(root.val)
            inorder(root.right)
            
            
        inorder(root)
        # print(self.nums, sorted(self.nums))
        return self.nums == sorted(self.nums) and len(self.nums) == len(set(self.nums))
            
            
