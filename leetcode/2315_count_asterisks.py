class Solution:
    def countAsterisks(self, s: str) -> int:

        pair_counter = 0
        
        ast_not_in_pair = ""

        for char in s:
            if char == "|":
                pair_counter += 1
            if pair_counter % 2 == 0:
                if char == "*":
                    ast_not_in_pair += char

        
        return len(ast_not_in_pair)