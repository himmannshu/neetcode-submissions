class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(list)
        s = set(nums)
        visited = set()
        for num in nums:
            if num not in d and num not in visited:
                visited.add(num)
                tmp = num + 1
                d[num] = []
                while tmp in s:
                    d[num].append(tmp)
                    visited.add(tmp)
                    tmp += 1
            elif num + 1 in d:
                d[num] = [num + 1] + d[num + 1]
        ans = 0
        for k,v in d.items():
            ans = max(ans, len(v) + 1)

        return ans