class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = []

        for ch in number:
            if ch.isdigit():
                digits.append(ch)
        
        result = []
        i = 0

        while len(digits) - i > 4:
            result.append("".join(digits[i:i+3]))
            i += 3
        
        remaining = len(digits) - i

        if remaining == 4:
            result.append("".join(digits[i:i+2]))
            result.append("".join(digits[i+2:i+4]))
        else:
            result.append("".join(digits[i:]))
        
        return "-".join(result)
        