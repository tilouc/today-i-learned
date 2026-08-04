class Solution(object):
    def sortedSquares(self, nums):

        n = len(nums)

        for i in range(n):
            nums[i] *= nums[i]
            
        nums.sort()

        return nums