class Solution:
    def maxPower(self, s: str) -> int:
        
        max_length = 1
        current_length = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current_length += 1
            
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        
        return max(max_length, current_length)