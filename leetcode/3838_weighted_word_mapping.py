class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        alphabet_sorted = alphabet[::-1]

        mapped_chars = ""

        total = 0

        result = 0

        for word in words:
            for letter in word:
                total += weights[alphabet.index(letter)]
            result = total % 26
            mapped_chars += alphabet_sorted[result]
            total = 0

        return mapped_chars