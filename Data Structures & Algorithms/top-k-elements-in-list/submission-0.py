class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1
        l = []
        for key, v in num_dict.items():
            l.append((-v, key))
        heapq.heapify(l)
        ans = []
        while k > 0:
            val = heapq.heappop(l)
            ans.append(val[1])
            k -= 1
        
        return ans