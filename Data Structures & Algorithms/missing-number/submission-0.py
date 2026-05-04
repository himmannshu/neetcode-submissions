class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       # 2 ways to do it:
       # declare a arr[n + 1], go through nums and update arr[nums[i]] = 1
       # in second pass, find arr index for which arr[index] == 0
       # 2nd way - use math
       n = len(nums)
       nums_sum = sum(nums)
       total_sum = (n * (n + 1))//2

       return total_sum - nums_sum