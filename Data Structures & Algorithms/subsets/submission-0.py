class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ans = []
        running_list = []

        def recurs(idx):
            if idx >= n:
                ans.append(running_list.copy())
                return
            
            running_list.append(nums[idx])
            recurs(idx + 1)
            running_list.pop()
            recurs(idx + 1)

        recurs(0)
        return ans
