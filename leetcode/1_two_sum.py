class Solution(object):
    def twoSum(self, nums, target):

        n = len(nums)

        target_list = []

        for i in range(n):
            for j in range(n):
                if (nums[i] + nums[j] == target) and (i != j):
                    if ((i not in target_list) and (j not in target_list)):
                        target_list.append(i)
                        target_list.append(j)
                    

        return target_list