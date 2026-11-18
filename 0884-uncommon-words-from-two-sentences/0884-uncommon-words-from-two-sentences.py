class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words = (s1 + " " + s2).split()

        word_count = Counter(words)

        res = []

        for word, count in word_count.items():

            if count == 1:
                res.append(word)
        
        return res