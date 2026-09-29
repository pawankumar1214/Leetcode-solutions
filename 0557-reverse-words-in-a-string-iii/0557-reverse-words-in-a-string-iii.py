class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words and reverse each word
        words = s.split()
        reversed_words = [word[::-1] for word in words]

        return ' '.join(reversed_words)