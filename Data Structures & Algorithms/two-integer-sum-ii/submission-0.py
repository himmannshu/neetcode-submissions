class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            num_sum = numbers[start] + numbers[end]
            if num_sum > target:
                end -= 1
            elif num_sum < target:
                start += 1
            else:
                return [start + 1, end + 1]