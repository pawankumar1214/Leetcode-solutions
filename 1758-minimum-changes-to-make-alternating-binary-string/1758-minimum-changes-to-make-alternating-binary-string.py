class Solution:
    def minOperations(self, s: str) -> int:
        changes_start0 = 0
        changes_start1 = 0

        for i, ch in enumerate(s):
            expected0 = '0' if i % 2 == 0 else '1'
            expected1 = '1' if i % 2 == 0 else '0'

            if ch != expected0:
                changes_start0 += 1
            if ch != expected1:
                changes_start1 += 1
        
        return min(changes_start0, changes_start1)