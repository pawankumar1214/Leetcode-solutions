class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        n_str = str(n)
        result = []

        for i in range(len(n_str)):
            result.append(n_str[-(i + 1)])
            if (i+1) % 3 == 0 and (i + 1) != len(n_str):
                result.append(".")
        return "".join(result[::-1])