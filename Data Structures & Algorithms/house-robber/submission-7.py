class Solution:
    def rob(self, nums: List[int]) -> int:
        # at each house, we have a choice whether to rob or not
        #self.ans = 0

        n = len(nums)
        memo = [-1] * n
        def recurse(idx):
            if idx >= n:
                return 0
            if memo[idx] != -1:
                return memo[idx]
            memo[idx] = max(recurse(idx + 1), nums[idx] + recurse(idx + 2))
            # we decide to rob
            #self.ans = max(self.ans, total + nums[idx])
            #recurse(idx + 2, total + nums[idx])
            #recurse(idx + 1, total)
            return memo[idx]
        
        #recurse(0,0)
        return recurse(0)