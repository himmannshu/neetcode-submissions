class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def dfs(tmp, flags):
            if len(tmp) == n:
                ans.append(tmp.copy())
                return
            
            for i, flag in enumerate(flags):
                if not flag:
                    tmp.append(nums[i])
                    flags[i] = True
                    dfs(tmp, flags)
                    flags[i] = False
                    tmp.pop()
        dfs([], [False for i in range(n)])

        return ans
