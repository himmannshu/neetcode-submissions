class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            """
            sorted_str = ''.join(sorted(st))
            if sorted_str not in anagram_dict:
                anagram_dict[sorted_str] = []
            anagram_dict[sorted_str].append(st)
            """
            count = [0]*26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            anagram_dict[tuple(count)].append(s)
        return anagram_dict.values()