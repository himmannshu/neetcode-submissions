class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        idx = 0
        l = len(s2)
        m = defaultdict(int)
        for i in range(len(s1)):
            m[s1[i]] += 1

        while idx < l:
            tmp, curr = m.copy(), idx
            while curr < l and s2[curr] in tmp:
                tmp[s2[curr]] -= 1
                if tmp[s2[curr]] == 0:
                    del tmp[s2[curr]]
                curr += 1
            if len(tmp) == 0:
                return True
            idx += 1
        return False