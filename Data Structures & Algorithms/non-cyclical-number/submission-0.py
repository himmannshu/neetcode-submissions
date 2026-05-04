class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n not in nums and n != 1:
            nums.add(n)
            digit_sum = 0
            temp_num = n

            while temp_num != 0:
                digit_sum += pow(temp_num % 10, 2)
                temp_num = temp_num // 10

            n = digit_sum
        
        if n == 1:
            return True
        else:
            return False