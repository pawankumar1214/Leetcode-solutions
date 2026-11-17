class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        upper_count = sum(1 for ch in word if 'A' <= ch <= 'Z')

        if upper_count == n:
            return True
        
        if upper_count == 0:
            return True
        
        if upper_count == 1 and 'A' <= word[0] <= 'Z':
            return True
        
        return False