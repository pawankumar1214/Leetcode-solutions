class Solution:
    def captureForts(self, forts: list[int]) -> int:
        prev = -1
        result = 0

        for i in range(len(forts)):
            if forts[i] != 0:
                if prev != -1 and forts[i] != forts[prev]:
                    result = max(result, i-prev-1)
                prev = i
        return result