class Solution:
    def scoreOfString(self, s: str) -> int:
        
        s_list = list(s)

        s_l = len(s_list) - 1

        score = 0

        i = 0

        for char in range(0, s_l):
            score += abs(ord(s_list[i]) - ord(s_list[i + 1]))
            i += 1
        
        return score