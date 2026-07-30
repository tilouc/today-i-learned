class Solution(object):
    def runningSum(self, nums):

        running_sum = 0
        nums_summed = []

        for index in range(len(nums)):
	        running_sum += nums[index]
	        nums_summed.append(running_sum)
	    
        return nums_summed