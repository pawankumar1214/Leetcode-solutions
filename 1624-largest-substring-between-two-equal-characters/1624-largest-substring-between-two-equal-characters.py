class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        first_index = {}
        max_len = -1

        for i, ch in enumerate(s):
            if ch in first_index:
                max_len = max(max_len, i - first_index[ch] - 1)
            else:
                first_index[ch] = i
        
        return max_len

        