# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        overall_max = 0

        def ff(root: TreeNode):
            nonlocal overall_max
            
            if root is None: return 0
        
            right_subtree = ff(root.right)
            left_subtree = ff(root.left)
            overall_max = max(overall_max, right_subtree + left_subtree)
        
            return 1 + max(right_subtree, left_subtree)

        ff(root)
        return overall_max
    
