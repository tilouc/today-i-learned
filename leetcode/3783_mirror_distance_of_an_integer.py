class Solution:
    def mirrorDistance(self, n: int) -> int:

        def reverse(n):

            n_str = str(n)

            n_str = n_str[::-1]

            n_rev = int(n_str)

            return n_rev

        mirror_distance = abs(n - reverse(n))

        return mirror_distance