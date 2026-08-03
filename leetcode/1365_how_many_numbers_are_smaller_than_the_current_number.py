class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        smaller = []
        counter = 0
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range((len_nums - 1), -1, -1):
                if j != i:
                    if nums[j] < nums[i]:
                        counter += 1
            
            smaller.append(counter)
            counter = 0
        
        return smaller