class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:

        num1_l = []

        num2_l = []

        for num in range(1, n + 1):
            if num % m != 0:
                num1_l.append(num)
            elif num % m == 0:
                num2_l.append(num)
            
        num1 = sum(num1_l)

        num2 = sum(num2_l)

        return num1 - num2