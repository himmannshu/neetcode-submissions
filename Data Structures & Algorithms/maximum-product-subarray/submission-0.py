class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Kadane's algo
        currMin, currMax = 1, 1
        prodMax = -float('inf')

        for num in nums:
            tmp = currMin * num
            currMin = min(tmp, currMax * num, num)
            currMax = max(currMax * num, num, tmp)
            prodMax = max(currMax, prodMax)
        return prodMax
        