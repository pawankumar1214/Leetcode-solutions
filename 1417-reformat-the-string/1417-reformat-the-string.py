class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []

        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                digits.append(ch)
        
        if abs(len(letters) - len(digits)) > 1:
            return ""
        
        result = []

        if len(letters) > len(digits):
            turn_letter = True
        else:
            turn_letter = False
        
        i = 0
        j = 0

        while i < len(letters) or j < len(digits):
            if turn_letter:
                result.append(letters[i])
                i += 1
            
            else:
                result.append(digits[j])
                j += 1
            
            turn_letter = not turn_letter
        return "".join(result)