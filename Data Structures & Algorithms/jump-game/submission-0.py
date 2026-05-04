class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # what is the max index that can be reached from the current ind
        max_ind = 0
        s = len(nums)
        for i in range(s):
            if max_ind < i:
                return False
            if max_ind >= s - 1:
                return True
            max_ind = max(max_ind, i + nums[i])
        return True