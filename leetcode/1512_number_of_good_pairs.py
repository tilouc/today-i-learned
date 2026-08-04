class Solution(object):
    def numIdenticalPairs(self, nums):
        len_nums = len(nums)

        good_pairs = 0

        for i in range(len_nums):
            for j in range(len_nums):
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1

        return good_pairs