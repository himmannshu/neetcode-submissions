class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True
        n = len(nums)
        i = 1
        max_jump = nums[0]

        while i < n and i <= max_jump:
            max_jump = max(max_jump, i + nums[i])
            if max_jump >= n - 1:
                return True
            i += 1
        
        return False
