class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common_count = Counter(words[0])

        for word in words[1:]:
            word_count = Counter(word)

            for char in common_count:
                common_count[char] = min(common_count[char], word_count[char])
        
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result