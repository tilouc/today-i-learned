class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        min_operations = 0

        for num in nums:
            if num % 3 != 0:
                min_operations += 1
        
        return min_operations