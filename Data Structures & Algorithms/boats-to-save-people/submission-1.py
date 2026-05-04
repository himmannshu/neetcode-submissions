class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i, j = 0, len(people) - 1
        ans = 0
        transported = 0
        while i < j:
            if people[i] + people[j] > limit:
                j -= 1
                ans += 1
                transported += 1
            else:
                i += 1
                j -= 1
                ans += 1
                transported += 2
        return ans + (len(people) - transported)
        