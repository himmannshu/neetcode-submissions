class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return len(nums)
        s = set(nums)
        ans = 1
        for num in nums:
            if (num - 1) not in s:
                temp = num
                cnt = 1
                while (temp + 1) in s:
                    temp += 1
                    cnt += 1
                ans = max(cnt, ans)
        return ans