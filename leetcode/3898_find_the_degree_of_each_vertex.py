class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        
        counter = 0

        ans = []
        
        for row in matrix:
            for number in row:
                if number == 1:
                    counter += 1
            
            ans.append(counter)
            counter = 0
        
        return ans