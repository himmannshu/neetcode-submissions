class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        stack = deque()
        results = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and stack[-1][0] < temp:
                t, idx = stack.pop()
                results[idx] = i - idx
            
            stack.append((temp, i))
        
        while len(stack) != 0:
            t, idx = stack.pop()
            results[idx] = 0
        
        return results