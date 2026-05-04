class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        suf = [0]*n
        pref[0] = suf[n - 1] = 1
        ans = []
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]
        for j in range(n - 2, -1, -1):
            suf[j] = suf[j + 1] * nums[j + 1]
        for i in range(n):
            ans.append(pref[i]*suf[i])
        return ans