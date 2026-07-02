class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_indices = sorted(range(len(score)), key=lambda i: score[i], reverse=True)
        ans = [""] * len(score)
        
        for rank, idx in enumerate(sorted_indices):
            if rank == 0:
                ans[idx] = "Gold Medal"
            elif rank == 1:
                ans[idx] = "Silver Medal"
            elif rank == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(rank + 1)
                
        return ans