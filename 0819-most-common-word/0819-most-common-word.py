class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)  # O(1) lookup instead of O(n)
        word_counter = {}

        normal_str = ''.join(char.lower() if char.isalnum() else ' ' for char in paragraph)

        for word in normal_str.split():
            if word not in banned_set:
                word_counter[word] = word_counter.get(word, 0) + 1
        
        return max(word_counter, key=word_counter.get)