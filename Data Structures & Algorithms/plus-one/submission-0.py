class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits) - 1
        carry = 1
        #for digit in digits[::-1]:
        while carry != 0 and n >= 0:
            tmp = digits[n] + carry
            digits[n] = tmp % 10
            carry = tmp // 10
            n -= 1
        
        if carry == 1:
            return [1] + digits
        return digits