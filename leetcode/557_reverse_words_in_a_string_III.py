class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()

        sentence = ""

        for word in words:
            word = word[::-1]
            sentence += word
            sentence += " "

        return sentence[:len(sentence) - 1]