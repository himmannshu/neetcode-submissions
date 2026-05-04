class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sol 1 - with sorting, O(n * m * log(m)), here m is the longest word
        # sol 2 - create ordinal count str - something like: cat -> a1c1t1 
        anagram_map = {}
        for s in strs:
            arr = [0]*26
            tmp = ""
            for ch in s:
                arr[ord(ch) - ord('a')] += 1
            
            for i in range(26):
                if arr[i] != 0:
                    tmp += chr(ord('a') + i) + str(arr[i])
            
            if tmp in anagram_map:
                anagram_map[tmp].append(s)
            else:
                anagram_map[tmp] = [s]
        ans = []
        for k, v in anagram_map.items():
            ans.append(v)
        
        return ans