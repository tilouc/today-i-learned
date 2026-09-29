class Solution:
    def alternateDigitSum(self, n: int) -> int:

        counter = 0

        digit_sum = 0

        n_str = str(n)

        n_str_rev = n_str[::-1]

        n_rev = int(n_str_rev)

        while n_rev:

            digit = n_rev % 10

            if counter % 2 == 0:
                digit_sum += digit
                
            else:
                digit_sum += -digit

            n_rev //= 10

            counter += 1
                
        return digit_sum