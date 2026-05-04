class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        st = 0
        end = len(s) - 1
        while st < end:
            if not s[st].isalnum():
                st += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[st] != s[end]:
                return False
            else:
                st += 1
                end -= 1
        return True