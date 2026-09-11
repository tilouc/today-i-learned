class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        
        n_str = str(n)

        n_str_l = []

        for i in range(len(n_str)):
            n_str_l.append(int(n_str[i]))
        
        n_str_s = set(n_str_l)

        n_str_sl = list(n_str_s)

        n_str_lf = []

        for j in range(len(n_str_sl)):
            n_str_sl[j] = n_str_sl[j] * n_str_l.count(n_str_sl[j])
            n_str_lf.append(n_str_sl[j])
        
        return sum(n_str_lf)