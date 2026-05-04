class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sol 1 - with sorting, O(n * m * log(m)), here m is the longest word
        # sol 2 - create ordinal count str - something like: cat -> a1c1t1 
        anagram_map = {}
        for s in strs:
            arr = [0]*26
            for ch in s:
                arr[ord(ch) - ord('a')] += 1
            tmp = tuple(arr)
            
            if tmp not in anagram_map:
                anagram_map[tmp] = []
            
            anagram_map[tmp].append(s)
        
        return anagram_map.values()