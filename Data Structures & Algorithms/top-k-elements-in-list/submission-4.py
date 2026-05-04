class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kv = defaultdict(int)
        for num in nums:
            kv[num] += 1
        # key = num, value = num_count
        n = len(nums)
        ans_list = [[] for i in range(n + 1)]
        for num, num_count in kv.items():
            ans_list[num_count].append(num)
        ans = []
        
        for i in range(n, 0, -1):
            for num in ans_list[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans
        

