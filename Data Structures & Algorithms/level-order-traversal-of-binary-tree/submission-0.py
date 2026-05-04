# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = deque()
        q.append([root])
        while q:
            level = q.popleft()
            tmp = []
            tmp2 = []
            for node in level:
                tmp.append(node.val)
                if node.left:
                    tmp2.append(node.left)
                if node.right:
                    tmp2.append(node.right)
            if len(tmp) != 0:
                ans.append(tmp)
            if len(tmp2) != 0:
                q.append(tmp2)
        return ans
            