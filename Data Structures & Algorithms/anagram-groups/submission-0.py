class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for st in strs:
            sorted_str = ''.join(sorted(st))
            if sorted_str not in anagram_dict:
                anagram_dict[sorted_str] = []
            anagram_dict[sorted_str].append(st)
        ans = []
        for k, v in anagram_dict.items():
            ans.append(v)
        return ans