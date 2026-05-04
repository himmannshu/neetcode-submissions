class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_set = set()
        cnt = 0
        idx = 0
        n = len(s)
        ans = 0

        while idx < n:
            if s[idx] in unique_set:
                ans = max(ans, idx - cnt)
                while cnt < idx and s[idx] in unique_set:
                    unique_set.remove(s[cnt])
                    cnt += 1
            unique_set.add(s[idx])
            idx += 1
        
        return max(ans, idx - cnt)