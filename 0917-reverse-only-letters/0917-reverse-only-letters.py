class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        list_char = list(s)
        l = 0
        r = len(s) - 1

        while l < r:
            if not list_char[l].isalpha():
                l += 1
            elif not list_char[r].isalpha():
                r -= 1
            else:
                temp = list_char[l]
                list_char[l] = list_char[r]
                list_char[r] = temp
                l += 1
                r -= 1
        return "".join(list_char)