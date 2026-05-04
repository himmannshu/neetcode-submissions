class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if n == 0: return 0

        max_jump = 0
        ans = 0
        
        for i, jump in enumerate(nums):
            if i + jump > max_jump:
                max_jump = i + jump
                ans +=1 
            if max_jump >= n:
                return ans
        
        return -1