class Solution:
    def reorderSpaces(self, text: str) -> str:
        total_spaces = text.count(" ")

        words = text.split()

        if len(words) == 1:
            return words[0] + " " * total_spaces
        
        gaps = len(words) - 1

        spaces_between = total_spaces // gaps

        extra_spaces = total_spaces % gaps

        result = (" " * spaces_between).join(words)
        result += " " * extra_spaces

        return result