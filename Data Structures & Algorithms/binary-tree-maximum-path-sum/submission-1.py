class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        
        def traverse(node):
            if node is None:
                return 0 # Using 0 makes handling negatives much cleaner
            
            # If a child returns a negative path, we simply ignore it (take 0)
            l = max(traverse(node.left), 0)
            r = max(traverse(node.right), 0)
            
            # 1. Update the global answer with the arched path
            self.ans = max(self.ans, node.val + l + r)
            
            # 2. Return ONLY the single best branch to the parent
            return node.val + max(l, r)
            
        traverse(root)
        return self.ans