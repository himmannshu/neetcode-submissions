class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # frequency of each letter should match
        if len(s) != len(t):
            return False
        
        s_count = [0]*26
        t_count = [0]*26

        n = len(s)

        for i in range(n):
            s_count[ord(s[i]) - ord('a')] += 1
            t_count[ord(t[i]) - ord('a')] += 1            
        
        for i in range(26):
            if s_count[i] != t_count[i]:
                return False
        
        return True