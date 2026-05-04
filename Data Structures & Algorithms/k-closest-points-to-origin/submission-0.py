class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for x, y in points:
            dist = (x ** 2 + y ** 2) ** 0.5
            pq.append((dist, x, y))
        
        heapq.heapify(pq)
        ans = []
        while pq and k > 0:
            d, x, y = heapq.heappop(pq)
            ans.append((x, y))
            k -= 1
        
        return ans