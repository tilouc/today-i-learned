class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
    
        i = 0

        counter = 0

        while (sum(nums) % k != 0):
            if nums[i] != 0:
                nums[i] = nums[i] - 1
                counter += 1
            else:
                i +=1

        return counter