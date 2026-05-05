class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        def f(curr_sum, i, tmp):
            if curr_sum == target:
                ans.append(tmp.copy())
                return
            if i >= n or curr_sum > target:
                return
            
            tmp.append(nums[i])
            f(curr_sum + nums[i], i, tmp)
            tmp.pop()
            f(curr_sum, i + 1, tmp)
        
        f(0, 0, [])
        return ans
            