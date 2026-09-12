class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:

        return (ans := nums + nums[::-1])