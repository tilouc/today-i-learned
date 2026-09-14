class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        indices = []

        counter = 0
        for word in words:
            if x in word:
                indices.append(counter)
            counter += 1
        
        return indices