class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = ("qwertyuiop", "asdfghjkl", "zxcvbnm")
        out = []

        def isWordOnRow(word, row):
            for w in word.lower():
                if w not in row:
                    return False
            return True

        for word in words: 
            for row in keyboard:
                if isWordOnRow(word, row):
                    out.append(word)
                    break
        return out