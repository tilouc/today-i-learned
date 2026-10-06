class Solution:
    def reverseDegree(self, s: str) -> int:
        
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        reversed_alphabet = alphabet[::-1]

        reverse_degree = 0

        index = 1

        for letter in s:
            reverse_degree += (index) * (reversed_alphabet.index(letter) + 1)
            index += 1

        return reverse_degree