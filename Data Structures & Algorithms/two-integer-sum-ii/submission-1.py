class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, end = 0, len(numbers) - 1

        while s < end:
            tmp = numbers[s] + numbers[end]

            if tmp > target:
                end -= 1
            elif tmp < target:
                s += 1
            else:
                return [s + 1, end + 1]
        
        return -1