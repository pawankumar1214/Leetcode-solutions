class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_length = 0

        for word in words:
            word_count = Counter(word)
            is_valid = True

            for c in word_count:
                if word_count[c] > chars_count.get(c,0):
                    is_valid = False
                    break
                
            if is_valid:
                total_length += len(word)
        
        return total_length

        