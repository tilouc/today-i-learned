class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        candies_list = candies[:]

        n = len(candies)

        result = []

        for item in range(n):
            candies = candies_list[:]
            if (2 <= n <= 100 and 1 <= candies[item] <= 100 and 1 <= extraCandies <= 50):
                candies[item] += extraCandies
                if (candies[item] >= max(candies)):
                    result.append(True)
                else:
                    result.append(False)
        return result