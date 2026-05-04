class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []
        # keep a dict to figure out what is the last place a char occurs
        """
        s = "xyxxyzbzbbisl"
             0123456789   
        {x: 3, y: 4, z: 7, b: 9, i: 10, s: 11, l: 12}
        """
        char_idx = defaultdict(int)
        n = len(s)
        for i in range(n):
            char_idx[s[i]] = i
        
        l, idx, r = 0, 0, char_idx[s[0]]
        res = []
        while idx < n:
            r = max(r, char_idx[s[idx]])

            if r == idx:
                res.append(r - l + 1)
                l = r + 1
            
            idx += 1
        
        return res