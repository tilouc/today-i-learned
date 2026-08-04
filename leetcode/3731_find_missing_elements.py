class Solution(object):
    def findMissingElements(self, nums):

        n = len(nums)

        nums.sort()

        nums_small = nums[0]

        nums_large = nums[n-1]

        missing = []

        for num in range(nums_small, nums_large):
            if num not in nums:
                missing.append(num)
            
        missing.sort()

        return missing