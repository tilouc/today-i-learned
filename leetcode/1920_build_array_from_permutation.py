class Solution(object):
    def buildArray(self, nums):
        ans = []
        num_length = len(nums)
        for i in range(num_length):
            ans.append(nums[nums[i]])

        return ans