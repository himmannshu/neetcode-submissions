class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kv = defaultdict(int)
        for num in nums:
            kv[num] += 1
        
        kv_tuple = [(-1 * v, k) for k , v in kv.items()]
        
        heapq.heapify(kv_tuple)
        ans = []
        while k > 0:
            ans.append(heapq.heappop(kv_tuple)[1])
            k -= 1
        
        return ans
        

