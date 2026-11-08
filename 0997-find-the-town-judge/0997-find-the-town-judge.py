class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1
        
        in_degree = [0] * (n+1)
        out_degree = [0] * (n+1)

        for a,b in trust:
            out_degree[a] += 1
            in_degree[b] += 1
        
        for person in range(1, n+1):
            if out_degree[person] == 0 and in_degree[person] == n-1:
                return person
        
        return -1
