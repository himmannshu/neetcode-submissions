class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        cnt, n, st = 1, len(s), list()
        st.append(s[0])
        while cnt < n:
            if len(st) != 0 and ((s[cnt] == ')' and st[-1] == '(') or (s[cnt] == '}' and st[-1] == '{') or (s[cnt] == ']' and st[-1] == '[')):
                st.pop()
            else:
                st.append(s[cnt])
            cnt += 1
        return len(st) == 0