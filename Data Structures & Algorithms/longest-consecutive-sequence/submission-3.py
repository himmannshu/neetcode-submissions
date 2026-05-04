class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in nums:
            if (num - 1) not in s:
                temp = num
                cnt = 1
                while (temp + 1) in s:
                    temp += 1
                    cnt += 1
                ans = max(cnt, ans)
        return ans