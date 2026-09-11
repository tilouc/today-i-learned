class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        
        score = 0

        while n:
            score += n % 10
            n //= 10

        return score