class Solution(object):
    def findNumbers(self, nums):
        
        nums_len = len(nums)

        even_digits = 0

        for i in range(nums_len):
            if len(str(nums[i])) % 2 == 0:
                even_digits += 1

        return even_digits