class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # insert - when len(word1) < len(word2)
        # delete - len(word1) > len(word2)
        # replace - len(word1) == len(word2)
        """
        horse - h.   min(recurse[1..n])
        """
        l1 = len(word1)
        l2 = len(word2)
        memo = [[-1 for i in range(l2)]for j in range(l1)]
        # l1 * l2
        def recurse(idx1, idx2):
            if idx2 >= l2:
                return l1 - idx1
            if idx1 >= l1:
                return l2 - idx2
            
            if memo[idx1][idx2] != -1:
                return memo[idx1][idx2]
            # need to keep count of the operations somewhere
            if word1[idx1] == word2[idx2]:
                memo[idx1][idx2] = recurse(idx1 + 1, idx2 + 1)
                return memo[idx1][idx2]
            # if this is not the case, delete the character
            memo[idx1][idx2] = min(1 + recurse(idx1 + 1, idx2), 1 + recurse(idx1, idx2 + 1), 1 + recurse(idx1 + 1, idx2 + 1))
            
            return memo[idx1][idx2]
        
        return recurse(0,0)
            