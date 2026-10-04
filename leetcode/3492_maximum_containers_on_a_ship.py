class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        
        max_num = 0

        counter = 0

        while max_num < maxWeight and counter < n*n:
            max_num += w
            if max_num <= maxWeight:
                counter += 1
        
        return counter