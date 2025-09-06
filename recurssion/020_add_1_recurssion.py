class Solution:
    def helper(self, nums, i):
        if i == len(nums):
            return 1
        carry = self.helper(nums, i + 1)
        sum_val = carry + nums[i]
        nums[i] = sum_val % 10
        return sum_val // 10

    def plusOne(self, digits: List[int]) -> List[int]:
        final_carry = self.helper(digits, 0)
        if final_carry > 0:
            digits.insert(0, 1)
        return digits

