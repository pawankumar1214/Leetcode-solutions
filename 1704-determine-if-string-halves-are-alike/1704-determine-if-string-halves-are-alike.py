class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        set1 = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        counter = 0

        for i in range(0, len(s)//2):
            if s[i] in set1:
                counter += 1
        
        for i in range(len(s)//2, len(s)):
            if s[i] in set1:
                counter -= 1
        
        return counter == 0
        